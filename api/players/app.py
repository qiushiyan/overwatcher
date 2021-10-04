from fastapi import APIRouter, Query, Path
from fastapi.params import Depends
from typing import Optional
from db.db_session import db
from api.constants import Team, Hero


def other_query_params(skip: Optional[int] = Query(0, ge=0, description="rows to skip"),
                       limit: Optional[int] = Query(None, ge=1, description="maximum number of records")):
    return {"skip": skip, "limit": limit}


app_players = APIRouter()


@app_players.get("/info")
async def get_player_info_all(select_cols="*"):
    """
    get all players's personal information, including:

    - player name (game id)
    - player real name
    - birth date
    - country
    - status (active or inactive)
    """
    return db.fetch_player_info_all(select_cols)


@app_players.get("/info/{name}")
async def get_player_info(name: str, select_cols="*"):
    """
    get personal information of single player by name
    """
    return db.fetch_player_info(name, select_cols)


# @app_players.get("/stats/{name}")
# async def get_player_stat(name: str = Path(..., description="player name"), hero: Hero = Query(None, description="hero name"),  query_params: dict = Depends(common_query_params)):
#     """
#     get match statistics by player name (season 4 only)
#     """
#     return db.fetch_players()
