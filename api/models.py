from datetime import date
from typing import List, Union

from pydantic import BaseModel


class PlayerStats(BaseModel):
    names: Union[List[str], str] = None
    select_cols: Union[List[str], str] = None
    stats: Union[List[str], str] = None
    heroes: Union[List[str], str] = None
    maps: Union[List[str], str] = None

    class Config:
        schema_extra = {
            "example": {
                "names": ["leave"],
                "select_cols": ["hero_name", "stat_name", "stat_mean"],
                "stats": [
                    "all damage done",
                    "ability damage done",
                    "average time alive",
                ],
                "heroes": ["tracer", "echo"],
                "maps": "ilios",
            }
        }


class PlayerInfo(BaseModel):
    names: Union[List[str], str] = None
    select_cols: Union[List[str], str] = None
    countries: Union[List[str], str] = None
    teams: Union[List[str], str] = None
    roles: Union[List[str], str] = None
    status: Union[List[str], str] = None

    class Config:
        schema_extra = {
            "example": {
                "teams": ["shanghai dragons", "atlanta reign"],
                "roles": ["tank", "dps"],
            }
        }


class Map(BaseModel):
    names: Union[List[str], str] = None
    select_cols: Union[List[str], str] = None
    match_dates: Union[List[str], str] = None
    max_date: date = None
    min_date: date = None
    stages: Union[List[str], str] = None
    winners: Union[List[str], str] = None
    losers: Union[List[str], str] = None
    skip: int = 0
    limit: int = None

    class Config:
        schema_extra = {
            "example": {"names": ["lijiang tower"], "winners": ["shanghai dragons"]}
        }


class Match(BaseModel):
    select_cols: Union[List[str], str] = None
    player_names: Union[List[str], str] = None
    dates: List[str] = None
    max_date: str = None
    min_date: str = None
    team_names: Union[List[str], str] = None
    stats: Union[List[str], str] = None
    heroes: Union[List[str], str] = None
    maps: Union[List[str], str] = None
    match_id: Union[List[int], int] = None
    skip: int = 0
    limit: int = None

    class Config:
        schema_extra = {
            "example": {
                "team_names": ["dallas fuel"],
                "maps": ["blizzard world"],
                "heroes": ["winston", "moira"],
            }
        }
