from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base, relationship
from sqlalchemy import Column, Integer, String, ForeignKey, JSON
from typing import Dict


PG_CONN_URI = "postgresql+asyncpg://postgres:postgres@localhost/postgres"

engine = create_async_engine(PG_CONN_URI, echo=True)
Base = declarative_base()

class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(100), nullable=False)
    username = Column(String(50), nullable=False)
    email = Column(String(70), nullable=False)
    address = Column(JSON)
    zipcode = Column(String(70))
    geo = Column(JSON)
    phone = Column(String(50))
    website = Column(String(100))
    company = Column(JSON)

    posts = relationship("Post", back_populates="user")

class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String(100), nullable=False)
    body = Column(String, nullable=False)
    userId = Column(Integer, ForeignKey('users.id'), nullable=False)

    user = relationship("User", back_populates="posts")

async_session = sessionmaker(
    engine,
    class_=AsyncSession,
    expire_on_commit=False
)

async def init_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all) 
        await conn.run_sync(Base.metadata.create_all)

async def close_db():
    await engine.dispose()