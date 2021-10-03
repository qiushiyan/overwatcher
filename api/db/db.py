import sqlalchemy as db
import pandas as pd


class Database:
    def __init__(self, RDS_USER, RDS_PWD, RDS_URI):
        self.engine = db.create_engine(
            f"mysql+mysqlconnector://{RDS_USER}:{RDS_PWD}@{RDS_URI}:3306/overwatcher")

    def connect(self):
        self.con = self.engine.connect()

    def fetch_players(self):
        df = pd.read_sql("select * from player_info", self.con)
        return df.to_json()
