import os
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column
from sqlalchemy import ForeignKey, String, BigInteger, Float, DateTime
from sqlalchemy.ext.asyncio import AsyncAttrs, create_async_engine, async_sessionmaker
from datetime import datetime
from dotenv import load_dotenv

load_dotenv()
DATABASE = os.getenv('DATABASE')

engine = create_async_engine(url=DATABASE, echo=True)
async_session = async_sessionmaker(engine, expire_on_commit=False)

class Base(AsyncAttrs, DeclarativeBase):
    pass


class User(Base):
    __tablename__ = 'users'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id = mapped_column(BigInteger)
    create_at: Mapped[datetime] = mapped_column(DateTime, default=datetime.now())


class Subscription(Base):
    __tablename__ = 'subscriptions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str] = mapped_column(String(20))
    price: Mapped[float] = mapped_column(Float)
    period: Mapped[int] = mapped_column()


class UserSubscription(Base):
    __tablename__ = 'user_subscriptions'
    
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey('users.id'))
    subs: Mapped[int] = mapped_column(ForeignKey('subscriptions.id'))
    expires_at: Mapped[datetime] = mapped_column(DateTime)


async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)        
        