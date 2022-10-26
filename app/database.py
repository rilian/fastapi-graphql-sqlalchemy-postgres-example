import os
from os.path import exists
from dotenv import load_dotenv
from sqlalchemy import create_engine  # type: ignore
from sqlalchemy.ext.declarative import declarative_base  # type: ignore
from sqlalchemy.orm import sessionmaker  # type: ignore
import logging

logger = logging.getLogger()

# NOTE: for local development
if exists(".env"):
    logger.warn("\n'.env' file exists - loading dotenv")
    load_dotenv()

engine = create_engine(os.getenv("DB_STR"), echo=os.getenv("STAGE") != "prod")
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()
