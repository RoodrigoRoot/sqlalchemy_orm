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
    #metadata.drop_all(engine)
    #metadata.create_all(engine)
    with engine.connect() as connection:
        #insert_query = users.insert()
        #with open('users.json') as file:
           
           #users = json.load(file)
           #connection.execute(insert_query, users)
            #for user in users:
                #query = insert_query.values(**user)
                #connection.execute(query)
        #select_query = users.select(users.c.country=="Mexico")
        #result = connection.execute(select_query)
        select_query = select([
            users.c.id,
            users.c.email,
            users.c.name
        ]).where(
            and_(
                users.c.gender == "Female",
                or_(
                    users.c.country == "Mexico",
                    users.c.country == "Japan"
                )

            )
        ).order_by(
            desc(users.c.name)
        ).limit(2)
        result = connection.execute(select_query)
        for user in result.fetchall():
            print(user)
        