# main.py

import logging
from aiogram import executor
from handlers import dp

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Зациклим бот
if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
