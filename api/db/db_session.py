from .db import Database
from dotenv import load_dotenv
import os

load_dotenv()

db = Database(os.environ.get("RDS_USER"), os.environ.get(
    "RDS_PWD"), os.environ.get("RDS_URI"))
