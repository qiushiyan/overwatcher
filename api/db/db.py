from datetime import date
from typing import Dict, List

import pandas as pd
import sqlalchemy
from api.utils import first_dict_key, first_dict_value, safely


class Database:
    def __init__(self, database_url: str):
        self.engine = sqlalchemy.create_engine(
            f"postgresql+psycopg2://{database_url}",
        )
        self.__operators = {
            "eq": "=",
            "ge": ">=",
            "gt": ">",
            "le": "<=",
            "lt": "<",
            "ne": "!=",
            "in": "in",
        }

    def start(self):
        self.__con = self.engine.connect()

    def shutdown(self):
        self.__con.close()

    def parse_condition(self, condition):
        """
        generate sql-like where condition based on dictionary,
        for example, {"date": {"ge": "2021-01-01"}} --> date >= '2021-01-01'
        """
        col = first_dict_key(condition)
        op_pair = condition.get(col)
        op_name = first_dict_key(op_pair)
        op_value = first_dict_value(op_pair)
        value_type = op_pair.get("type")
        op = self.__operators.get(op_name)
        if op != "in":
            if value_type is None:
                return f"{col} {op} '{op_value}'"
            elif value_type == "numeric":
                return f"{col} {op} {op_value}"
        else:
            # could pass a scalar value in post request
            if value_type is None:
                if isinstance(op_value, list):
                    values = "(" + ", ".join(["'" + i + "'" for i in op_value]) + ")"
                    return f"{col} in {values}"
                else:
                    return f"{col} = '{op_value}'"
            elif value_type == "numeric":
                if isinstance(op_value, list):
                    values = "(" + ", ".join([i for i in op_value]) + ")"
                    return f"{col} in {values}"
                else:
                    return f"{col} = {op_value}"

    def compose_sql(
        self,
        from_table: str,
        select_cols: List[str],
        conditions: List[Dict[str, Dict]],
        skip: int = 0,
        limit: int = None,
    ):
        if select_cols is None:
            cols = "*"
        else:
            cols = ", ".join(select_cols)
        if len(conditions) >= 1:
            parsed_conditions = " and ".join(
                [self.parse_condition(condition) for condition in conditions]
            )
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
    def fetch_player_info(
        self,
        names: str,
        select_cols: List[str] = None,
        countries: List[str] = None,
        teams: List[str] = None,
        roles: List[str] = None,
        status: List[str] = None,
    ):
        conditions = []
        if names is not None:
            conditions.append({"player_name": {"in": names}})
        if countries is not None:
            conditions.append({"country": {"in": countries}})
        if teams is not None:
            conditions.append({"team_name": {"in": teams}})
        if roles is not None:
            conditions.append({"role": {"in": roles}})
        if status is not None:
            conditions.append({"status": {"in": status}})

        sql = self.compose_sql(
            from_table="player_info", select_cols=select_cols, conditions=conditions
        )
        df = pd.read_sql(sql, self.__con).fillna("")
        return df

    @safely
    def fetch_player_stats(
        self,
        names: str,
        select_cols: List[str],
        stats: List[str],
        heroes: List[str],
        maps: List[str],
    ):
        conditions = []
        if names is not None:
            conditions.append({"player_name": {"in": names}})
        if stats is not None:
            conditions.append(
                {
                    "stat_name": {"in": stats},
                }
            )
        if heroes is not None:
            conditions.append(
                {
                    "hero_name": {"in": heroes},
                }
            )
        if maps is not None:
            conditions.append({"map_name": {"in": maps}})

        sql = self.compose_sql(
            from_table="player_stats", select_cols=select_cols, conditions=conditions
        )
        df = pd.read_sql(sql, self.__con).fillna("")
        return df

    @safely
    def fetch_matches(
        self,
        select_cols: List[str],
        player_names: List[str],
        dates: List[date],
        max_date: date,
        min_date: date,
        team_names: List[str],
        stats: List[str],
        heroes: List[str],
        maps: List[str],
        match_id: int,
        skip: int,
        limit: int,
    ):
        conditions = []
        if player_names is not None:
            conditions.append({"player_name": {"in": player_names}})
        if dates is not None:
            dates = list(map(dates, str))
            conditions.append({"date": {"in": dates}})
        if max_date is not None:
            conditions.append({"date": {"le": str(max_date)}})
        if min_date is not None:
            conditions.append({"date": {"ge": str(min_date)}})
        if team_names is not None:
            conditions.append({"team_name": {"in": team_names}})
        if stats is not None:
            conditions.append({"stat_name": {"in": stats}})
        if heroes is not None:
            conditions.append({"hero_name": {"in": heroes}})
        if maps is not None:
            conditions.append({"map_name": {"in": maps}})
        if match_id is not None:
            conditions.append({"match_id": {"eq": match_id, "type": "numeric"}})

        sql = self.compose_sql(
            from_table="matches",
            select_cols=select_cols,
            conditions=conditions,
            skip=skip,
            limit=limit,
        )
        df = pd.read_sql(sql, self.__con).fillna("")
        return df

    @safely
    def fetch_maps(
        self,
        names: str,
        select_cols: List[str],
        match_dates: List[str],
        max_date: date,
        min_date: date,
        stages: List[str],
        winners: List[str],
        losers: List[str],
        skip: int = 0,
        limit: int = None,
    ):
        conditions = []
        if names is not None:
            conditions.append({"map_name": {"in": names}})
        if match_dates is not None:
            dates = [str(date) for date in match_dates]
            conditions.append({"match_date": {"in": dates}})
        if max_date is not None:
            conditions.append({"match_date": {"le": str(max_date)}})
        if min_date is not None:
            conditions.append({"match_date": {"ge": str(min_date)}})
        if stages is not None:
            conditions.append({"stage": {"in": stages}})

        if winners is not None:
            conditions.append({"map_winner": {"in": winners}})

        if losers is not None:
            conditions.append({"map_loser": {"in": losers}})

        sql = self.compose_sql(
            from_table="maps",
            select_cols=select_cols,
            conditions=conditions,
            skip=skip,
            limit=limit,
        )
        df = pd.read_sql(sql, self.__con).fillna("")
        return df
