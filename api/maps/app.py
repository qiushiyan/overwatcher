from fastapi import APIRouter, Query, Path
from fastapi.params import Depends
from typing import Optional, List
from api.utils import gen_response
from api.db.db_session import db

app_maps = APIRouter()


@app_maps.get("/{name}")
def get_maps(name: str):
    pass
