from sqlalchemy import Column, DateTime, Integer, String, Table, MetaData
from sqlalchemy.sql import func

metadata = MetaData()

notes = Table(
    "notes",
    metadata,
    Column("id", Integer, primary_key=True),
    Column("title", String(50)),
    Column("description", String(50)),
    Column("created_date", DateTime, default=func.now(), nullable=False),
)
