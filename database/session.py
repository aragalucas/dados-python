from app.sqlalchemy import create_engine
from app.sqlalchemy.ext.declarative import declarative_base
from app.sqlalchemy.orm import sessionmaker

DATABASE_URL = "mysql+pymysql://root:password@localhost:3306/senai_db"

engine = create_engine(DATABASE_URL, echo=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
