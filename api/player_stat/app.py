from fastapi import APIRouter, Query, Path
from fastapi.params import Depends
from typing import Optional, List
from api.utils import gen_response
from db.db_session import db
from api.constants import Hero

app_player_stat = APIRouter()


def other_query_params(
    select_cols: List[str] = Query(
        None, description="see below for available columns"),
    stat: List[str] = Query(None, description="""
statistics name, including but not limited to
- general statiscis such as 'time alived', 'time played', 'eliminations', 'deaths'
- hero-specific statistics such as 'scoped critical hits', 'inspire uptime' and 'healing accuracy'"""),
    hero: List[str] = Query(
        None, description="hero name"),
    map_: List[str] = Query(
        None, description="map name", alias="map"),
    skip: Optional[int] = Query(0, ge=0, description="rows to skip"),
    limit: Optional[int] = Query(
        None, ge=1, description="maximum number of records")):
    return {"select_cols": select_cols, "stat": stat, "hero": hero, "map_": map_, "skip": skip, "limit": limit}


@app_player_stat.get("/{name}")
async def get_player_stat(name: str = Path(..., description="player name"),
                          other_query_params: dict = Depends(other_query_params)):
    """
    get average match statistics by player name (season 4 only), on player-hero-map-stat level

    returns (when select_cols is not specified)

    - player_name
    - hero_name
    - map_name
    - stat_name
    - stat_mean (average value of that stat)
    - count (number of occurrences)
    """
    res = db.fetch_player_stat(name, **other_query_params)
    return gen_response(res)
