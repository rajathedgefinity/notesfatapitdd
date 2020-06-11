import os

from databases import Database
from sqlalchemy import create_engine


DATABASE_URL = os.getenv("DATABASE_URL")

# SQLAlchemy
engine = create_engine(DATABASE_URL)

database = Database(DATABASE_URL)
