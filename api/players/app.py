from fastapi import APIRouter
from db.db_session import db

app_players = APIRouter()


@app_players.get("/{name}")
async def get_player(name: str):
    return db.fetch_players()
