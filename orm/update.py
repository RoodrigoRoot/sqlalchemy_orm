from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, not_
from sqlalchemy.orm.exc import NoResultFound

from datetime import datetime

engine = create_engine("postgresql://rod:forever11@localhost/pythondb")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    created_at = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.username     
Session = sessionmaker(engine)
session = Session()

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    user1 = User(username='User1', email='user1@gmail.com')
    user2 = User(username='User2', email='user2@gmail.com')
    user3 = User(username='User3', email='user3@gmail.com')
    session.add(user1)
    session.add(user2)
    session.add(user3)

    session.commit()

    user = session.query(User).filter(User.id ==1).first()
    user.username = "Rodrigo"
    user.email = "leyco@gmail.com"
    session.add(user)
    session.commit()

    session.query(User).filter(
        User.id == 2
    ).update(
        {
            User.username: 'Francisco',
            User.email: 'juego@hotmail.com'
        }
    )
    session.commit()