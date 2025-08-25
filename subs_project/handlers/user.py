from aiogram.types import Message, CallbackQuery
from aiogram.filters import CommandStart
from aiogram import Router, F
from keyboards.user_kb import user_main
import database.requests as rq

user = Router()

@user.message(CommandStart())
async def cmd_start(message: Message):
    user_id = message.from_user.id
    await rq.set_user(user_id)
    await message.answer('Добро пожаловать!\n\n'
                         'Сначала оформите подписку:', reply_markup=await user_main())
