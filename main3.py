from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column, Integer, String, DateTime
from sqlalchemy import select
from sqlalchemy import and_, or_, not_
from sqlalchemy import asc, desc
from datetime import datetime
import json

engine = create_engine('postgresql://rod:forever11@localhost/pythondb')
metadata = MetaData()

#Users
users = Table(
    'users',
    metadata,
    Column('id', Integer, primary_key=True),
    Column('age', Integer),
    Column('country', String(20), nullable=False),
    Column('email', String(50), nullable=False),
    Column('gender', String(6), nullable=False),
    Column('name', String(50), nullable=False)



)

if __name__ == "__main__":

    with engine.connect() as connection:
        with open('users.json') as file:   
           connection.execute(users.insert(), json.load(file))

        select_query = select(
            [users.c.name]

        ).where(
            users.c.id == 1
        )
        result = connection.execute(select_query)
        user = result.fetchone()
        print(user)
        