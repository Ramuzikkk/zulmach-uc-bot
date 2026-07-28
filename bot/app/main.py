import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.client.session.aiohttp import AiohttpSession
from aiohttp_socks import ProxyConnector


BOT_TOKEN = os.getenv("BOT_TOKEN")
PROXY = os.getenv("PROXY")

if not BOT_TOKEN:
    raise ValueError("BOT_TOKEN не найден")


dp = Dispatcher()


def menu_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text="💎 Купить UC")
    builder.button(text="📦 Мои заказы")
    builder.button(text="🆘 Поддержка")

    builder.adjust(1)

    return builder.as_markup(resize_keyboard=True)


@dp.message(Command("start"))

async def start(message: Message):

    await message.answer(

        "🔥 Добро пожаловать в ZULMACH UC BOT!\n\n"

        "💎 Продажа PUBG Mobile UC\n"

        "⚡ Быстрое пополнение 24/7\n"

        "🛡 Надёжная поддержка\n\n"

        "━━━━━━━━━━━━━━\n"

        "💎 КАТАЛОГ UC\n"

        "━━━━━━━━━━━━━━\n\n"

        "🟦 60 UC — 99₽\n"

        "🟦 325 UC — 499₽\n"

        "🟦 660 UC — 899₽\n"

        "🟦 1800 UC — 2299₽\n\n"

        "👇 Выберите нужный пакет UC в меню",

        reply_markup=menu_keyboard()

    )


async def main():

    proxy = os.getenv("PROXY")

    if proxy:

        session = AiohttpSession(proxy=proxy)

        bot = Bot(

            token=BOT_TOKEN,

            session=session

        )

        print("🌐 SOCKS5 proxy enabled")

    else:

        bot = Bot(token=BOT_TOKEN)
        print("🌐 Running without proxy")

    print("🤖 ZULMACH UC BOT started")

    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
