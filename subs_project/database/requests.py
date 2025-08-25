from database.models import async_session, User, Subscription, UserSubscription
from sqlalchemy import select


async def set_user(user_id):
    async with async_session() as session:
        user = await session.scalar(select(User).where(User.user_id == user_id))
        
        if not user:
            user = User(
                user_id=user_id
            )
            session.add(user)
            await session.commit()
        
        return user    

async def get_subscriptions():
    async with async_session() as session:
        result = await session.execute(select(Subscription))
        subs = result.scalars().all()
        return subs
    
async def get_subscription(sub_id):
    async with async_session() as session:
        return await session.scalar(select(Subscription).where(Subscription.id == sub_id))    
        