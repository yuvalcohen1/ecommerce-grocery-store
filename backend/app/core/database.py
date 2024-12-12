from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app.core.config import settings
from sqlalchemy.orm import declarative_base

Base = declarative_base()

engine = create_engine(settings.DATABASE_URL, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()
