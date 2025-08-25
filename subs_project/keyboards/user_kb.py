from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.types import WebAppInfo

async def user_main():
    kb = ReplyKeyboardBuilder()
    kb.button(text='Открыть', web_app=WebAppInfo(url='https://form-app-puce.vercel.app/'))
    return kb.as_markup(resize_keyboard=True)