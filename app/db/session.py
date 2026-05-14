from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from app.core.config import settings

engine = create_engine(settings.GHOSTDOC_DB_URL)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
