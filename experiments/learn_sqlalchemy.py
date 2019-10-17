import os

'''
SQLAlchemy tutorials:
1. https://docs.sqlalchemy.org/en/13/orm/tutorial.html
2. https://leportella.com/english/2019/01/10/sqlalchemy-basics-tutorial.html#engine-connection
'''


from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String

Base = declarative_base()


class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True)
    name = Column(String)
    fullname = Column(String)
    nickname = Column(String)
    age = Column(Integer)

    def __repr__(self):
        return "<User(name='%s', fullname='%s', nickname='%s', age='%i')>" % \
            (self.name, self.fullname, self.nickname, self.age )

testuser = User(name='test', fullname='testothy jones', nickname='testy', age=19)


from sqlalchemy import create_engine
engine = create_engine(os.getenv('DATABASE_URL'), echo=True)
Base.metadata.create_all(engine)

from sqlalchemy.orm import sessionmaker
Session = sessionmaker(bind=engine)

print("\n\n\nStarting session and creating users...")
session = Session()

def addUser(userObj):
    copy = session.query(User).filter_by(name=userObj.name).first()
    if(not copy):
        session.add(userObj)
    else:
        print("User with that name already exists. Not adding.\n")

addUser(testuser)
addUser(User(name='test2', fullname='testothy jones 2', nickname='testy', age=19))
addUser(User(name='test3', fullname='testothy jones 3', nickname='testy', age=19))

print("\n\n\nCommit session...")
session.commit()

print("\n\n\nQuerying for users...")
query = session.query(User)
print("\n\n\nFound %i users in the system." % (query.count()))