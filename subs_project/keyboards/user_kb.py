from aiogram.utils.keyboard import ReplyKeyboardBuilder

async def user_main():
    kb = ReplyKeyboardBuilder()
    kb.button(text='Открыть')
    return kb.as_markup(resize_keyboard=True)