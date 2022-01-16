from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine
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
            (self.name, self.fullname, self.nickname, self.age)


testuser = User(name='test', fullname='testothy jones',
                nickname='testy', age=19)


engine = create_engine(os.getenv('DATABASE_URL'), echo=True)
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)

print("\n\n\nStarting session and creating users...")
session = Session()


def addUser(userObj):
    copy = session.query(User).filter_by(name=userObj.name).first()
    if(not copy):
        session.add(userObj)
        session.commit()
    else:
        print("User with that name already exists. Not adding.\n")

addUser(testuser)
addUser(User(name='test2', fullname='testothy jones 2', nickname='testy', age=19))
addUser(User(name='test3', fullname='testothy jones 3', nickname='testy', age=19))


print("\n\n\nQuerying for users...")
query = session.query(User)
print("\n\n\nFound %i users in the system." % (query.count()))

'''
Query a set of users within the system.
'''
def printdb():
    count = 0
    print("Users in System:")
    for user in query:
        count = count + 1
        print("%i: %s, %s" % (count, user.name, user.fullname))
printdb()

'''
Todo: 
1. Add new user, find in table.
2. Modify existing user.
3. Modify a list of items inside the user. See:
   https://stackoverflow.com/questions/49784883/saving-complex-objects-in-sqlalchemy
4. Delete a user.
'''

#1
addUser(User(name='mitch', fullname='mitch haines bryant', nickname='golden mitch', age=26))

'''
addUser(User(name='Abe', fullname='Abraham Lincoln', nickname='Dark Phoenix', age=32))
addUser(User(name='Henry', fullname='Henry Ford', nickname='The Enlightened', age=43))
addUser(User(name='Humphrey', fullname='Humphrey Bogart', nickname='Goodwill', age=43))
'''

for user in session.query(User).filter_by(name='mitch'):
    print("Found %s '%s' %s (ID:%i) in the database." % (user.name, user.nickname, user.fullname, user.id))

printdb()

#2
mitch = session.query(User).filter_by(name='mitch').first()
mitch.name = "o%so2" % (mitch.name)
session.commit()

printdb()


#3
'''
See second SQLAlchemy test file.
'''

#4
for user in session.query(User).filter_by(name='omitcho2'):
    session.delete(user)

session.commit()

printdb()

session.close()