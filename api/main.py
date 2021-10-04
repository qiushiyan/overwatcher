from fastapi import FastAPI
import uvicorn
from fastapi.openapi.docs import get_swagger_ui_html
from fastapi.staticfiles import StaticFiles
from player_info import app_player_info
from player_stat import app_player_stat
from db.db_session import db
from config import Settings

settings = Settings()


app = FastAPI(title=settings.app_title,
              description=settings.app_description, version=settings.app_version,
              docs_url=None, redoc_url=None)


app.mount("/static", StaticFiles(directory="static"), name="static")


@app.on_event("startup")
def startup():
    db.connect()


@app.on_event("shutdown")
def shutdown():
    db.close()

# swagger theming


@app.get("/docs", include_in_schema=False)
def overridden_swagger():
    return get_swagger_ui_html(openapi_url=app.openapi_url,
                               title=app.title + " - Swagger UI",
                               oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
                               swagger_css_url="/static/swagger-ui.css",
                               swagger_js_url="/static/swagger-ui-bundle.js")


app.include_router(app_player_stat, prefix="/player_stat",
                   tags=["average match statistics of players (season 4)"])

app.include_router(app_player_info, prefix="/player_info",
                   tags=["personal information of players"])
if __name__ == '__main__':
    uvicorn.run('main:app', host='0.0.0.0', port=8000,
                reload=True, debug=True, workers=1)