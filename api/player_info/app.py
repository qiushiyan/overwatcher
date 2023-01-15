from typing import List

from api.db.db_session import db
from api.models import PlayerInfo
from api.utils import gen_response
from fastapi import APIRouter, Query

app_player_info = APIRouter()


@app_player_info.get("/{name}")
async def get_player_info(
    name: str,
    select_cols: List[str] = Query(
        None, description="default to all, see above for available columns"
    ),
):
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
    res = db.fetch_player_info(names=name, select_cols=select_cols)
    return gen_response(res)


@app_player_info.get("")
async def get_player_info_all(
    names: List[str] = Query(None, description="included players"),
    select_cols: List[str] = Query(
        None, description="default to all, see above for available columns"
    ),
    countries: List[str] = Query(None),
    teams: List[str] = Query(None),
    roles: List[str] = Query(None),
    status: List[str] = Query(None),
):
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
    res = db.fetch_player_info(names, select_cols, countries, teams, roles, status)
    return gen_response(res)


@app_player_info.post("")
def get_player_info_post(player_info: PlayerInfo):
    """
    get player info with post request
    """
    res = db.fetch_player_info(**player_info.dict())
    return gen_response(res)
