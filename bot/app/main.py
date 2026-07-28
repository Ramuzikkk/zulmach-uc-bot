import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from aiogram.utils.keyboard import ReplyKeyboardBuilder
from aiogram.client.session.aiohttp import AiohttpSession
from aiohttp_socks import ProxyConnector
from aiogram.types import FSInputFile

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
    
    photo = FSInputFile("assets/uc_banner.jpg")
   
    await message.answer_photo(

    photo=photo,

    caption=(

        "🔥 <b>ZULMACH UC BOT</b>\n\n"

        ...

    ),

    reply_markup=uc_keyboard(),

    parse_mode="HTML"

)
        "🔥 <b>ZULMACH UC BOT</b>\n\n"
        "💎 <b>PUBG MOBILE UC</b>\n\n"
        "━━━━━━━━━━━━━━\n"
        "💎 60 UC\n"
        "💰 Цена: 99₽\n\n"

        "💎 325 UC\n"
        "💰 Цена: 499₽\n\n"

        "💎 660 UC\n"
        "💰 Цена: 899₽\n\n"

        "💎 1800 UC\n"
        "💰 Цена: 2299₽\n"
        "━━━━━━━━━━━━━━\n\n"

        "⚡ Быстрое пополнение\n"
        "🛡 Поддержка 24/7\n\n"
        "👇 Выберите пакет UC:",
        
        reply_markup=uc_keyboard(),
        parse_mode="HTML"
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
