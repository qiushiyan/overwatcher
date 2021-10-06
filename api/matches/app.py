from fastapi import APIRouter, Query, Path
from typing import List
from datetime import date
from api.utils import gen_response
from api.db.db_session import db

app_matches = APIRouter()


@app_matches.get("/")
async def get_matches(
    select_cols: List[str] = Query(
        None, description="default to all, see below for available columns"),
    player_names: List[str] = Query(None, description="players"),
    dates: List[date] = Query(None, description="match date"),
    min_date: date = Query(
        None, description="min date, season 4 starts on 2021-04-16"),
    max_date: date = Query(
        None, description="max date, season 4 ends on 2021-09-26"),
    team_names: List[str] = Query(None, description="teams"),
    stats: List[str] = Query(None, description=f"""
statistics name, for example
- general statiscis such as 'time alived', 'time played', 'eliminations', 'deaths'
- hero-specific statistics such as 'scoped critical hits', 'inspire uptime' and 'healing accuracy'

see full list at <https://github.com/qiushiyan/overwatcher#stats>
"""),
    heroes: List[str] = Query(
        None,  description="included heroes, see full list at <https://github.com/qiushiyan/overwatcher#heroes>"),
    maps: List[str] = Query(
        None, description="included maps, see full list at <https://github.com/qiushiyan/overwatcher#maps>"),
    match_id: int = Query(
        None, description="map id, can be used to join on maps"),
    skip: int = Query(0, ge=0, description="rows to skip"),
    limit: int = Query(
        None, ge=1, description="maximum number of records")):
    """
    get average match statistics (season 4 only)

    returns

    - player_name
    - hero_name
    - map_name
    - stat_name
    - stat_mean (average value of that stat)
    - count (number of matches)
    """
    res = db.fetch_matches(select_cols, player_names, dates, min_date,
                           max_date, team_names, stats, heroes, maps, match_id, skip, limit)
    return gen_response(res)
