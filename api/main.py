from contextlib import asynccontextmanager
import uvicorn
from fastapi import FastAPI
from fastapi.openapi.docs import get_swagger_ui_html

from api.config import Settings
from api.db.db_session import db
from api.maps import app_maps
from api.matches import app_matches
from api.player_info import app_player_info
from api.player_stat import app_player_stats

settings = Settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    db.start()
    yield
    db.shutdown()


app = FastAPI(
    title=settings.app_title,
    description=settings.app_description,
    version=settings.app_version,
    docs_url=None,
    redoc_url=None,
    lifespan=lifespan,
)


@app.get("/")
def hello():
    return {
        "msg": "Welcome to overwatch league statistics api, available routes are /player_info, /player_stats, /matches and /maps, visit https://github.com/qiushiyan/overwatcher for documentation",
    }


# swagger theming


@app.get("/docs", include_in_schema=False)
def overridden_swagger():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
    )


app.include_router(
    app_player_info, prefix="/player_info", tags=["player personal information"]
)

app.include_router(
    app_player_stats, prefix="/player_stats", tags=["average player statistics"]
)

app.include_router(app_matches, prefix="/matches", tags=["per match player statistics"])

app.include_router(
    app_maps, prefix="/maps", tags=["per round map attack/defend statistics"]
)

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True, workers=1)
