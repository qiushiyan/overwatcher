from pydantic import BaseModel, Field
from typing import List
from datetime import date


class PlayerStats(BaseModel):
    names: List[str] or str = None
    select_cols: List[str] or str = None
    stats: List[str] or str = None
    heroes: List[str] or str = None
    maps: str = None

    class Config:
        schema_extra = {
            "example": {
                "names": "leave",
                "select_cols": ["hero_name", "stat_name", "stat_mean"],
                "stats": ["all damage done", "ability damage done", "average time alive"],
                "heroes": ["tracer", "echo"],
                "maps": "ilios"
            }
        }


class PlayerInfo(BaseModel):
    names: List[str] or str = None
    select_cols: List[str] or str = None
    countries: List[str] or str = None
    teams: List[str] or str = None
    roles: List[str] or str = None
    status: List[str] or str = None

    class Config:
        schema_extra = {
            "example": {
                "teams": ["shanghai dragons", "atlanta reign"],
                "roles": ["tank", "dps"]
            }
        }


class Map(BaseModel):
    names: List[str] or str = None
    select_cols: List[str] or str = None
    match_dates: List[str] or str = None
    max_date: date = None
    min_date: date = None
    stages: List[str] or str = None
    winners: List[str] or str = None
    losers: List[str] or str = None
    skip: int = 0
    limit: int = None

    class Config:
        schema_extra = {
            "example": {
                "names": ["lijiang tower"],
                "winners": ["shanghai dragons"]
            }
        }


class Match(BaseModel):
    select_cols: List[str] or str = None
    player_names: List[str] or str = None
    dates: List[str] = None
    max_date: str = None
    min_date: str = None
    team_names: List[str] or str = None
    stats: List[str] or str = None
    heroes: List[str] or str = None
    maps: List[str] or str = None
    match_id: int or List[int] = None
    skip: int = 0
    limit: int = None

    class Config:
        schema_extra = {
            "example": {
                "team_names": ["dallas fuel"],
                "maps": ["blizzard world"],
                "heroes": ["winston", "moira"]
            }
        }
