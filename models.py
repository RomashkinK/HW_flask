import os
import atexit
import datetime
from sqlalchemy import create_engine
from sqlalchemy.orm import DeclarativeBase, sessionmaker, Mapped, mapped_column
from sqlalchemy import Column, String, DateTime, Integer, func

POSTGRES_USER=os.getenv('POSTGRES_USER', 'postgres')
POSTGRES_PASSWORD=os.getenv('POSTGRES_PASSWORD', 'password')
POSTGRES_DB=os.getenv('POSTGRES_DB', 'flask_hw')
POSTGRES_HOST=os.getenv('POSTGRES_HOST', '127.0.0.1')
POSTGRES_PORT=os.getenv('POSTGRES_PORT', '5431')

PG_DSN = f'postgresql://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_HOST}:{POSTGRES_PORT}/{POSTGRES_DB}'


engine = create_engine(PG_DSN)
Session = sessionmaker(bind=engine)

class Base(DeclarativeBase):
    pass

class Advertisement(Base):
    __tablename__ = 'advertisement'
    
    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    title: Mapped[str] = mapped_column(String(100), index=True, nullable=False)
    description: Mapped[str] = mapped_column(String(1000), nullable=False)
    creation_datetime: Mapped[datetime.datetime] = mapped_column(DateTime, server_default=func.now())
    owner: Mapped[str] = mapped_column(nullable=False)


Base.metadata.create_all(engine)

atexit.register(engine.dispose)

    