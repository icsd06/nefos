from sqlalchemy import create_engine
from sqlalchemy import exc
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os
import time

SQLALCHEMY_DATABASE_URL = os.environ.get('DATABASE_URL')

#SQLALCHEMY_DATABASE_URL = "mysql+pymysql://root@localhost:3306/myfastdb"

def get_engine():
    engine = create_engine(db_url)
    return engine

while True:
    try:
        engine = get_engine()
        result = engine.execute('SELECT 1')
        break
    except sqlalchemy.exc.OperationalError:
        print('MySQL server not available, retrying in 5 seconds...')
        time.sleep(5)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()



