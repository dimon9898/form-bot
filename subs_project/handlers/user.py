import json
from aiogram.types import Message, CallbackQuery, LabeledPrice
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

@user.message(F.web_app_data)
async def get_webapp(message: Message):
    text = message.web_app_data.data
    data = json.loads(text)
    fullname = str(data['fullname'])
    email = str(data['email'])
    subs_id = int(data['tarif'])
    subs = await rq.get_subscription(subs_id)
    await message.answer(f'Имя: {fullname}\n'
                         f'Почта: {email}\n'
                         f'Тариф: {subs.name}')
    price = [LabeledPrice(label='Оплата за подписку', amount=subs.price * 100)]
    await message.bot.send_invoice(
        chat_id=message.from_user.id,
        title=subs.name,
        description=f'{subs.period} дней',
        payload=f'subscription_{subs.id}_{message.from_user.id}_{fullname}_{email}',
        currency='RUB',
        provider_token='1744374395:TEST:b9879982909d7c1bd39c',
        prices=price,
        start_parameter='create_order'
    )   
    
    