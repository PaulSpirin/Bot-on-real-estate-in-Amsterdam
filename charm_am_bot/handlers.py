# handlers.py

import keyboard
import text
from config import BOT_TOKEN, PHOTO_POST_MAP, PHOTO_PIPELINE, DISTRICT_LIST
from models import model, predict_price
import logging
from aiogram import Bot, Dispatcher, types, executor

# Включаем логирование
logging.basicConfig(level=logging.INFO)

# Объект бота
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await message.reply(text=text.greet)  # Отправляем приветственное сообщение
    await message.answer(text.menu, reply_markup=keyboard.menu)  # Отправляем меню


# Обработчик команд выхода в меню
@dp.message_handler(lambda message: message.text.lower() in ['меню', 'выйти в меню', 'назад в меню', 'назад'])
async def menu_handler(message: types.Message):
    await message.answer(text.menu, reply_markup=keyboard.menu)


# Обработчик команды "Информация о боте"
@dp.callback_query_handler(lambda c: c.data == "text_inform")
async def inform_text_handler(callback_query: types.CallbackQuery):
    await bot.send_chat_action(callback_query.from_user.id, action=types.ChatActions.TYPING)  # Выводим "typing..."
    await callback_query.answer()
    await callback_query.message.answer(text.text_inform)


# Обработчик команды "Карты районов"
@dp.callback_query_handler(lambda c: c.data == "district_map")
async def district_map_handler(callback_query: types.CallbackQuery):
    await bot.send_chat_action(callback_query.from_user.id, action=types.ChatActions.TYPING)
    await callback_query.answer()
    # Отправляем текст и изображение
    await callback_query.message.answer_photo(
        photo=open(PHOTO_POST_MAP, 'rb'),
        caption=text.district_map)


# Обработчик команды "Информация для DS"
@dp.callback_query_handler(lambda c: c.data == "ds_inform")
async def inform_text_handler(callback_query: types.CallbackQuery):
    await bot.send_chat_action(callback_query.from_user.id, action=types.ChatActions.TYPING)
    await callback_query.answer()
    await callback_query.message.answer_photo(photo=open(PHOTO_PIPELINE, 'rb'),
                                              caption=text.ds_inform)


# Обработчик команды "Связь с модератором"
@dp.callback_query_handler(lambda c: c.data == "help_inform")
async def inform_text_handler(callback_query: types.CallbackQuery):
    await bot.send_chat_action(callback_query.from_user.id, action=types.ChatActions.TYPING)
    await callback_query.answer()
    await callback_query.message.answer(text.help_inform)


# Обработчик команды "Начать предсказание" (Вывод текста/примера)
@dp.callback_query_handler(lambda c: c.data == "start_bot_gen")
async def start_bot_gen_handler(callback_query: types.CallbackQuery):
    try:
        await bot.send_chat_action(callback_query.from_user.id, action=types.ChatActions.TYPING)
        await callback_query.answer()
        await callback_query.message.answer(text.start_bot_gen)  # Tекст с инструкцией
    except Exception as e:
        await callback_query.message.answer(f"Произошла ошибка: {e}")  # Обработка ошибок


# Обработчик команды "Модели"
@dp.message_handler(lambda message: message.text and ',' in message.text)
async def handle_input_data(message: types.Message):
    try:
        # Разбираем текст от пользователя на параметры
        input_values = message.text.split(',')

        # Проверяем количество введенных параметров
        if len(input_values) != 3:
            raise ValueError("Введите все три параметра: площадь, количество комнат, код района")

        # Проверяем на ввод целых чисел (отсекаем str)
        try:
            area, rooms, district = map(int, input_values)
        except ValueError:
            raise ValueError("Пожалуйста, введите целые числа для площади, количества комнат и кода района")

        # Проверяем корректность введенных данных
        if not (15 <= area <= 600):
            raise ValueError("Площадь должна быть от 15 до 600 включительно")
        if not (1 <= rooms <= 15):
            raise ValueError("Количество комнат должно быть от 1 до 15 включительно")
        if district not in DISTRICT_LIST:
            raise ValueError("Некорректный код района")


        # Функцию для предсказания цены из файла model.py
        predicted_price = predict_price(model, area, rooms, district)

        await message.answer(
            f"Предсказанная стоимость квартиры: €{format(int(predicted_price), ',').replace(',', ' ')}")

        # Добавляем клавиатуру с главным меню для возврата пользователя
        await message.answer("Вернуться в главное меню?", reply_markup=keyboard.menu)
    except ValueError as e:
        await message.answer(f"Ошибка ввода данных: {e}")
    except Exception as e:
        await message.answer(f"Произошла ошибка: {e}")
