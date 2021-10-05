from fastapi import APIRouter, Query, Path
from typing import Optional, List
from datetime import date
from api.utils import gen_response
from api.db.db_session import db

app_matches = APIRouter()


@app_matches.get("/")
async def get_matches(
    select_cols: List[str] = Query(
        None, description="default to all, see below for available columns"),
    player_names: List[str] = Query(None, description="players"),
    date: date = Query(None, description="match date"),
    min_date: date = Query(
        None, description="min date, season 4 starts on 2021-04-16"),
    max_date: date = Query(
        None, description="max date, season 4 ends on 2021-09-26"),
    team_names: List[str] = Query(None, description="teams"),
    stats: List[str] = Query(None, description="""
statistics name, including but not limited to
- general statiscis such as 'time alived', 'time played', 'eliminations', 'deaths'
- hero-specific statistics such as 'scoped critical hits', 'inspire uptime' and 'healing accuracy'"""),
    heroes: List[str] = Query(
        None, description="hero name"),
    maps: List[str] = Query(
        None, description="map name", alias="map"),
    skip: Optional[int] = Query(0, ge=0, description="rows to skip"),
    limit: Optional[int] = Query(
        None, ge=1, description="maximum number of records")):
    """
    get average match statistics (season 4 only)

    returns (when select_cols is not specified)

    - player_name
    - hero_name
    - map_name
    - stat_name
    - stat_mean (average value of that stat)
    - count (number of occurrences)
    """
    res = db.fetch_matches(select_cols, player_names, date, min_date,
                           max_date, team_names, stats, heroes, maps, skip, limit)
    return gen_response(res)
