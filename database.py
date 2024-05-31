from sqlalchemy.engine.url import URL
from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(DATABASE_URL, connect_args={"check_same_thread": False})

# DB = {
#     'drivername': 'pgsql',
#     'host': '127.0.0.1',
#     'port': '3306',
#     'username': os.environ['DBUNAME'],
#     'password': os.environ['DBPASS'],
#     'database': os.environ['DBNAME'],
#     'query': {'charset':'utf8'}
# }

# engine = create_engine(URL(**DB))

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()