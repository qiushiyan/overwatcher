from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Overwatcher"
    app_description: str = "API based on Overwatch League Stats Lab,  provides player, team, match, and teamfight statistics"
    app_version: str = "0.1.0"
