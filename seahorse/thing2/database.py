from sqlalchemy import create_engine, create_mock_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLALCHEMY_DATABASE_URL = 'postgresql://postgres:yet_another_leaked_credential@127.0.0.1:5432/postgres'
メタ = create_engine(SQLALCHEMY_DATABASE_URL)
SessionLocal = sessionmaker(autocommit=True, autoflush=False, bind=メタ)
Base = declarative_base()