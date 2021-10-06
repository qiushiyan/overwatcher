from fastapi import APIRouter, Query
from typing import List
from api.utils import gen_response
from api.db.db_session import db
from datetime import date

app_maps = APIRouter()


@app_maps.get("/{name}")
def get_map(name: str,
            select_cols: List[str] = Query(
                None, desciption="default to all, see below for available columns"),
            match_dates: List[date] = Query(None, description="match date"),
            stages: List[str] = Query(
                None, description="owl stage"),
            winners: List[str] = Query(None, description="map winner"),
            losers: List[str] = Query(None, description="map loser"),
            skip: int = 0,
            limit: int = None):
    """
    get per-round attack/defend statistics by map name (matches accross all 4 seasons)

    returns:

    - stage (e.g, season 1 stage1, season2 stage1, season2 playoff. See full list at <https://github.com/qiushiyanoverwatcher#stages)
    - match_id
    - game_number (number of games played)
    - match_winner
    - map_winner
    - map_loser
    - map_name
    - map_round
    - wining_team_final_map_score
    - losing_team_final_map_score
    - control_round_name
    - team_one_name (attacker on non-assult maps)
    - team_two_name (defender on non-attack maps)
    - attacker_payload_distance
    - defender_payload_distance
    - attacker_time_banked
    - defender_time_banked
    - attacker_control_percent
    - defender_control_percent
    - attacker_round_end_score
    - defender_round_end_score
    - map_type
    - match_date
    - round_duration (in minutes)
    """
    res = db.fetch_maps(name, select_cols, match_dates,
                        stages, winners, losers, skip, limit)
    return gen_response(res)
