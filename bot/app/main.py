import asyncio
from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command


BOT_TOKEN = "ВСТАВИМ_ПОЗЖЕ"


bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🔥 Добро пожаловать в ZULMACH UC BOT!\n\n"
        "Здесь можно купить UC для PUBG Mobile."
    )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
