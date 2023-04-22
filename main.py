from handers.main_handler import main_handler
from aiogram import Bot, Dispatcher, executor

from key_holder import token


async def a(dp: Dispatcher):
    print("Бот запущен")
    await main_handler(dp)


def start_bot():
    bot = Bot(token=token)
    dp = Dispatcher(bot)
    executor.start_polling(dp, on_startup=a)
