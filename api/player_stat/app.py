from fastapi import APIRouter, Query, Path
from fastapi.params import Depends
from typing import List
from api.utils import gen_response
from api.db.db_session import db
from api.models import PlayerStats

app_player_stats = APIRouter()


def other_query_params(
    select_cols: List[str] = Query(
        None, description="default to all, see above for available columns"),
    stats: List[str] = Query(None, description="""
included statistics, for example
- general statiscis such as 'time alived', 'time played', 'eliminations', 'deaths'
- hero-specific statistics such as 'scoped critical hits', 'inspire uptime' and 'healing accuracy'

see full list at <https://github.com/qiushiyan/overwatcher#stats>
"""),
    heroes: List[str] = Query(
        None, description="included heroes, see full list at <https://github.com/qiushiyan/overwatcher#heroes>"),
    maps: List[str] = Query(
        None, description="included maps, see full list at <https://github.com/qiushiyan/overwatcher#maps>"),
):
    return {"select_cols": select_cols, "stats": stats, "heroes": heroes, "maps": maps, }


@app_player_stats.get("/{name}")
async def get_player_stats(name: str = Path(..., description="player name"),
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
    res = db.fetch_player_stats(name, **other_query_params)
    return gen_response(res)


@app_player_stats.post("")
async def get_player_stats_post(player: PlayerStats):
    res = db.fetch_player_stats(**player.dict())
    return gen_response(res)


@app_player_stats.get("")
async def get_player_stats_all(
        names: List[str] = Query(None, description="included players"),
        other_query_params: dict = Depends(other_query_params)):
    """
    get average match statistics of all players
    """
    res = db.fetch_player_stats(names, **other_query_params)
    return gen_response(res)
