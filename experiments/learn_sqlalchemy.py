import os

'''
See here for the excellent SQLAlchemy tutorial:
https://docs.sqlalchemy.org/en/13/orm/tutorial.html
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
'''
session.add(testuser)
session.add(User(name='test2', fullname='testothy jones 2', nickname='testy', age=19))
session.add(User(name='test3', fullname='testothy jones 3', nickname='testy', age=19))
'''

print("\n\n\nCommit session...")
session.commit()

print("\n\n\nQuerying for users...")
query = session.query(User)
print("\n\n\nFound %i users in the system." % (query.count()))