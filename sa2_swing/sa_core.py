import os

from sqlalchemy import create_engine, MetaData, select, Table
from sqlalchemy import Column, Integer, String


SQLALCHEMY_URI = os.getenv("DATABASE_URL")

engine = create_engine(SQLALCHEMY_URI)


# CREATE TABLES WITH CORE
user_table = Table(
    "user",
    metadata_obj,
    Column('id', Integer, primary_key=True),
    Column('name', String(30)),
    Column('fullname', String)
)

meta = MetaData()
# Can also do individual tables which looks like:
# students = Table('student', meta, autoload=True, autoload_with=engine)
# users = Table('user', meta, autoload=True, autoload_with=engine)

# Automagically reflect all the tables
meta.reflect(bind=engine)
students = meta.tables["student"]
users = meta.tables["user"]

query = (
    select([students.c.id, users.c.firstname])
    .where(users.c.student_id == students.c.id)
    .where(users.c.firstname == "Daniel")
)

results = None
with engine.connect() as conn:
    results = conn.execute(query).fetchall()

for row in results:
    print(row)

