from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, String, DateTime, Integer, ForeignKey
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import and_, or_, not_
from sqlalchemy.orm.exc import NoResultFound
from sqlalchemy.orm import relationship

from datetime import datetime

engine = create_engine("postgresql://rod:forever11@localhost/pythondb")
Base = declarative_base()

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    username = Column(String(20), nullable=False, unique=True)
    email = Column(String(80), nullable=False, unique=True)
    courses = relationship('Course', backref='user')
    created_at = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.username     

class Course(Base):
    __tablename__ = "courses"
    id = Column(Integer, primary_key = True)
    title = Column(String(50), nullable=False)
    user_id = Column(ForeignKey('users.id'))
    created_at = Column(DateTime, default=datetime.now())

    def __str__(self):
        return self.title
Session = sessionmaker(engine)
session = Session()

if __name__ == "__main__":
    Base.metadata.drop_all(engine)
    Base.metadata.create_all(engine)
    
    user1 = User(username='User1', email='user1@gmail.com')
    user2 = User(username='User2', email='user2@gmail.com')
    user1.courses.append(Course(title='Curso1', user_id=user1.id))
    user1.courses.append(Course(title='Curso2', user_id=user1.id))
    user2.courses.append(Course(title='Curso3', user_id=user1.id))

    session.add(user1)
    session.add(user2)
    
    session.commit()

    