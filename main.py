from sqlalchemy import create_engine
from sqlalchemy import MetaData
from sqlalchemy import Table
from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime

engine = create_engine('postgresql://rod:forever11@localhost/pythondb')
metadata = MetaData()

#Users
users = Table(
    'users',
    metadata,
    Column('id', Integer(), primary_key=True),
    Column('username', String(), index=True, nullable=False),
    Column('email', String(), nullable=False),
    Column('created_at', DateTime(), default=datetime.now())

)

if __name__ == "__main__":
    #metadata.drop_all(engine)
    #metadata.create_all(engine)
    with engine.connect() as connection:
#    print(users.c.id)
        query_insert = users.insert().values(
            username = 'user11',
            email='example@gmail.com'
        )
        connection.execute(query_insert)
