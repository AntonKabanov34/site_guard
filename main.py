# Рабочая версия асинхронщины
import asyncio
import aiogram.utils.markdown as md
from aiogram import Bot, Dispatcher, types
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from aiogram.types import ParseMode
import requests

API_TOKEN = '6345400660:AAHc65ldRUQvFFoRknNa6iTeiuP81TiA9u0'  # Замените на свой API токен
chat_id = '166476724'  # Замените на ID вашего чата

# Инициализация бота и диспетчера
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

# Функция для отправки кода ответа от сайта
async def send_response_code():
    url = 'https://vk.com'  # URL сайта, код ответа которого вы хотите получить
    response = requests.get(url)
    response_code = response.status_code

    await bot.send_message(chat_id, f'Код ответа от сайта {url}: {response_code}')

# Основной цикл бота
async def main():
    while True:
        await send_response_code()
        await asyncio.sleep(60)  # Ожидание 60 секунд перед повторным выполнением

if __name__ == '__main__':
    asyncio.run(main())
