from datetime import datetime
from sqlalchemy import MetaData, Table, Column
from sqlalchemy.types import Integer, String, TIMESTAMP
from sqlalchemy.dialects.postgresql.types import BYTEA

metadata = MetaData()

user = Table(
    "user",
    metadata,
    Column("uid", Integer, primary_key=True, autoincrement=True),
    Column("name", String, nullable=False),
    Column("surname", String, nullable=False),
    Column("username", String, nullable=False),
    Column("hashed_password", BYTEA, nullable=False),
    Column("salt", BYTEA, nullable=False),
    Column("registered_at", TIMESTAMP, default=datetime.utcnow),
    Column("email", String),
)
