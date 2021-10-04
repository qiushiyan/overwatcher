from pydantic import BaseSettings


class Settings(BaseSettings):
    app_title: str = "Overwatcher"
    app_description: str = f"""
## Overwatch League Match, Maps and Players API

The data comes from two sources:

- [Overwatch League Stats Lab](https://overwatchleague.com/zh-cn/statslab) including match and map statistics for all 4 seasons, currently only season 4 match statistics is presented in the app

- [Liquipedia Player Wiki](https://liquipedia.net/overwatch/Players) including players' personal information
    """
    app_version: str = "0.1.0"