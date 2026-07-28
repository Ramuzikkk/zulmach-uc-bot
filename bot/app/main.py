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
        "Пополнение PUBG Mobile UC быстро и удобно.",
        reply_markup=menu_keyboard(),
    )


@dp.message()
async def menu(message: Message):
    if message.text == "💎 Купить UC":
        await message.answer(
            "💎 Каталог UC скоро будет доступен."
        )

    elif message.text == "📦 Мои заказы":
        await message.answer(
            "📦 У вас пока нет заказов."
        )

    elif message.text == "🆘 Поддержка":
        await message.answer(
            "🆘 Поддержка ZULMACH\n\n"
            "Telegram: @zulmach_support"
        )

    else:
        await message.answer(
            "Выберите пункт меню ниже 👇",
            reply_markup=menu_keyboard(),
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
