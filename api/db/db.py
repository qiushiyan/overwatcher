from datetime import date
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
            "ne": "!=",
            "in": "in"
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
        if op != "in":
            if (value_type := op_pair.get("type")) is None:
                return f"{col} {op} '{op_value}'"
            elif value_type == "numeric":
                return f"{col} {op} {op_value}"
        else:
            values = "(" + ", ".join(["'" + i + "'" for i in op_value]) + ")"
            return f"{col} in {values}"

    def compose_sql(self,
                    from_table: str,
                    select_cols: List[str],
                    conditions: List[Dict[str, Dict]],
                    skip: int = 0,
                    limit: int = None):
        if select_cols is None:
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

    @safely
    def fetch_player_stats(self, name: str, select_cols: List[str], stats: List[str], heroes: List[str], maps: List[str]):
        conditions = [{"player_name": {"eq": name}}]
        if stats is not None:
            conditions.append({
                "stat_name": {"in": stats},
            })
        if heroes is not None:
            conditions.append({
                "hero_name": {"in": heroes},
            })
        if maps is not None:
            conditions.append({
                "map_name": {"in": maps}
            })

        sql = self.compose_sql(from_table="player_stats",
                               select_cols=select_cols,
                               conditions=conditions)
        df = pd.read_sql(sql, self.__con).fillna("")
        return df

    @safely
    def fetch_player_stats_all(self,  select_cols: List[str], stats: List[str], heroes: List[str], maps: List[str]):
        conditions = []
        if stats is not None:
            conditions.append({
                "stat_name": {"in": stats},
            })
        if heroes is not None:
            conditions.append({
                "hero_name": {"in": heroes},
            })
        if maps is not None:
            conditions.append({
                "map_name": {"in": maps}
            })
        sql = self.compose_sql(from_table="player_stats",
                               select_cols=select_cols,
                               conditions=conditions)
        df = pd.read_sql(sql, self.__con)
        return df

    @safely
    def fetch_matches(self, select_cols: List[str], player_names: List[str], date: date, min_date: date, max_date: date, team_names: List[str], stats: List[str], heroes: List[str], maps: List[str], match_id: int, skip: int, limit: int):
        conditions = []
        if player_names is not None:
            conditions.append({
                "player_name": {"in": player_names}
            })
        if date is not None:
            conditions.append({
                "date": {"eq": date}
            })
        if min_date is not None:
            conditions.append({
                "date": {"ge": min_date}
            })
        if max_date is not None:
            conditions.append({
                "date": {"le": max_date}
            })
        if team_names is not None:
            conditions.append({
                "team_name": {"in": team_names}
            })
        if stats is not None:
            conditions.append({
                "stat_name": {"in": stats}
            })
        if heroes is not None:
            conditions.append({
                "hero_name": {"in": heroes}
            })
        if maps is not None:
            conditions.append({
                "map_name": {"in": maps}
            })
        if match_id is not None:
            conditions.append({
                "match_id": {"eq": match_id, "type": "numeric"}
            })

        sql = self.compose_sql(from_table="matches",
                               select_cols=select_cols,
                               conditions=conditions,
                               skip=skip,
                               limit=limit)
        df = pd.read_sql(sql, self.__con).fillna("")
        return df
