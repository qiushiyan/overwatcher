from fastapi import FastAPI
import uvicorn
from players import app_players
from db.db_session import db


app = FastAPI(description="overwatch league statistics api")


@app.on_event("startup")
def startup():
    db.connect()


@app.on_event("shutdown")
def shutdown():
    db.close()


app.include_router(app_players, prefix="/players",
                   tags=["player statistics and meta info"])


if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000,
                reload=True, debug=True, workers=1)
