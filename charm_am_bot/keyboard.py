# keyboard.py

from aiogram.types import InlineKeyboardButton, InlineKeyboardMarkup, KeyboardButton, ReplyKeyboardMarkup

menu = [
    [InlineKeyboardButton(text='Информация о боте', callback_data='text_inform'),
    InlineKeyboardButton(text='Карты районов', callback_data='district_map')],
    [InlineKeyboardButton(text='Информация для DS', callback_data='ds_inform'),
    InlineKeyboardButton(text='Начать предсказание', callback_data='start_bot_gen')],
    [InlineKeyboardButton(text='Связь с модератором', callback_data='help_inform')]

]
menu = InlineKeyboardMarkup(inline_keyboard=menu)
exit_kb = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text='Выйти в меню')]], resize_keyboard=True)
iexit_kb = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text='Выйти в меню', callback_data='menu')]])
