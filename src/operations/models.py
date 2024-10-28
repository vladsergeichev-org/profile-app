from datetime import datetime
from sqlalchemy import MetaData, Table, Column, ForeignKey
from sqlalchemy.types import Integer, String, TIMESTAMP

from users.models import user

metadata = MetaData()

operation = Table(
    "operation",
    metadata,
    Column("id", Integer, primary_key=True, autoincrement=True),
    Column("user_id", Integer, ForeignKey(user.c.uid)),
    Column("replenish", Integer),
    Column("total_replenish", Integer),
    Column("total_amount", Integer),
    Column("date", TIMESTAMP),
)