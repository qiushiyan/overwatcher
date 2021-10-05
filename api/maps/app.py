from fastapi import APIRouter, Query, Path
from fastapi.params import Depends
from typing import Optional, List
from api.utils import gen_response
from api.db.db_session import db

app_maps = APIRouter()


@app_maps.get("/{name}")
def get_map(name: str,
            select_cols: List[str] = Query(None),
            team_names: List(str) = Query(
                None, description="participating teams"),
            winner: str = Query(None, description="map winner"),
            loser: str = Query(None, description="map loser")):
    """
    get attack/defend round statistics by map name (matches accross all 4 seasons)

    returns:

    - stage (e.g, season 1 stage1, season2 stage1, season2 playoff. See full list at )
    - match_id
    - game number (number of games played)
    """
    pass
