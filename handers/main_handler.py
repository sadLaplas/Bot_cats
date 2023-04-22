from aiogram.types import Message
from aiogram import Dispatcher


async def main_handler(dp: Dispatcher):
    @dp.message_handler(text=["Привет!", "Пока"])
    async def msg(message: Message):
        await message.answer(f"{message.text}, {message.from_user.username}")

    @dp.message_handler(commands="start")
    async def start(message: Message):
        await message.answer("Это тестовый бот")
