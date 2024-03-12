from .db import Database
from dotenv import load_dotenv
import os

load_dotenv()

db = Database(os.environ.get("DATABASE_URL"))
