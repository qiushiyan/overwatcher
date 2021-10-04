import sqlalchemy
import pandas as pd
from typing import Dict, List
from api.utils import first_dict_key, first_dict_value, safely


class Database:
    def __init__(self, RDS_USER: str, RDS_PWD: str, RDS_URI: str):
        self.engine = sqlalchemy.create_engine(
            f"mysql+mysqlconnector://{RDS_USER}:{RDS_PWD}@{RDS_URI}:3306/overwatcher")
        self.__operators = {
            "eq": "=",
            "ge": ">=",
            "gt": ">",
            "le": "<=",
            "lt": "<",
            "ne": "!="
        }

    def connect(self):
        self.__con = self.engine.connect()

    def parse_condition(self, condition):
        """
        generate sql-like where condition based on dictionary,
        for example, {"date": {"ge": "2021-01-01"}} --> date >= '2021-01-01'
        """
        col = first_dict_key(condition)
        op_pair = condition.get(col)
        op_name = first_dict_key(op_pair)
        op_value = first_dict_value(op_pair)
        op = self.__operators.get(op_name)
        return f"{col} {op} '{op_value}'"

    def compose_sql(self,
                    from_table: str,
                    select_cols: List[str],
                    conditions: List[Dict[str, Dict]],
                    skip: int = 0,
                    limit: int = None):
        if "*" in select_cols:
            cols = "*"
        else:
            cols = ", ".join(select_cols)
        if len(conditions) >= 1:
            parsed_conditions = " and ".join(
                [self.parse_condition(condition) for condition in conditions])
        else:
            parsed_conditions = "true"
        if limit is None:
            return f"""
            SELECT {cols}
            FROM {from_table}
            WHERE {parsed_conditions}
            """
        else:
            return f"""
            SELECT {cols}
            FROM {from_table}
            WHERE {parsed_conditions}
            LIMIT {skip}, {limit}
            """

    @safely
    def fetch_player_info(self, name: str, select_cols: List[str]):
        sql = self.compose_sql(from_table="player_info",
                               select_cols=select_cols,
                               conditions=[
                                   {"player_name": {"eq": name}}])
        df = pd.read_sql(sql, self.__con).fillna("")
        return df

    @safely
    def fetch_player_info_all(self, select_cols: List[str], skip: int = 0, limit: int = None):
        sql = self.compose_sql(from_table="player_info",
                               select_cols=select_cols,
                               conditions=[],
                               skip=skip,
                               limit=limit)
        df = pd.read_sql(sql, self.__con).fillna("")
        return df
