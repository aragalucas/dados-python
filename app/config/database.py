from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from contextlib import contextmanager

db_user = "user"
db_password = "password"
db_host = "localhost"
db_port = "3306"
dn_name = "meu banco"

DATABASE_URL = f"mysql+pymysql:\\{db_user}:{db_password}@{db_host}:{db_port}/{db_name}"

db = create_engine(DATABASE_URL)
Session = sessionmaker(bind=db)
session = Session()

@contextmanager
def get_db():
    db = Session()
    try:
        yield db
        db.commmit()
    except Exception as erro:
        db.rollback()
        raise erro
    finally:
        db.close()