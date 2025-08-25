import os
import asyncio
from aiogram import Bot, Dispatcher
from dotenv import load_dotenv
from database.models import create_tables
from handlers.user import user

load_dotenv()

dp = Dispatcher()
TG_TOKEN = os.getenv('TG_TOKEN')



async def main():
    await create_tables()
    bot = Bot(token=TG_TOKEN)
    dp.include_router(user)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())