from fastapi import APIRouter, Query
from typing import List
from api.utils import gen_response
from api.db.db_session import db


app_player_info = APIRouter()


@app_player_info.get("/{name}")
async def get_player_info(name: str, select_cols: List[str] = Query(None, description="default to all, see below for available columns")):
    """
    get personal information by player name

    returns

    - player_name (game id)
    - player_real_name
    - birth
    - country
    - status (active or inactive)
    - team_name
    - earnings (total earnings in the overwatch career)
    - role (support, dps or tank)
    - signature_hero (heroes the player is most known for, separated by new lines)
    - age
    """
    res = db.fetch_player_info(name, select_cols)
    return gen_response(res)


@app_player_info.get("/")
async def get_player_info_all(select_cols: List[str] = Query(None, description="default to all, see below for available columns")):
    """
    get all players's personal information

    returns:

    - player_name (game id)
    - player_real_name
    - birth
    - country
    - status (active or inactive)
    - team_name
    - earnings (total earnings in the overwatch career)
    - role (support, dps or tank)
    - signature_hero (heroes the player is most known for, separated by new lines)
    - age
    """
    res = db.fetch_player_info_all(select_cols)
    return gen_response(res)
