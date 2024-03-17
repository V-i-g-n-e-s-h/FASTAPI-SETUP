from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import Session, sessionmaker, scoped_session

from config import config

username = config["DB"]["USERNAME"]
password = config["DB"]["PASSWORD"]
db_name = config["DB"]["DB_NAME"]
host = config["DB"]["HOST"]
port = config["DB"]["PORT"]

db_string = f"postgresql://{username}:{password}@{host}:{port}/{db_name}"

engine = create_engine(
    url=db_string,
    pool_size=20,
    max_overflow=0
)

base = declarative_base()
session = scoped_session(session_factory=sessionmaker(bind=engine))

def get_db():
    session_ = sessionmaker(bind=engine)
    session: Session = session_()
    session.autoflush = False

    try:
        yield session
    except:
        session.rollback()
    finally:
        session.close()
