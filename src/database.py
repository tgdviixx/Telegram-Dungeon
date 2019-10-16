import os
import sqlalchemy



class Database():
    '''Connects to a SQLAlchemy Database'''

    # Class variables shared by all instances.

    def __init__(self):
        # Instance variables unique to each instance.
        print(sqlalchemy.__version__)

    def connect(self):
        return True
