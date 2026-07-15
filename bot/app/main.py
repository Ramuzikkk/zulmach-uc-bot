import asyncio
import os

from aiogram import Bot, Dispatcher
from aiogram.types import Message
from aiogram.filters import Command
from aiogram.utils.keyboard import ReplyKeyboardBuilder

from app.products import PRODUCTS

BOT_TOKEN = os.getenv("BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()


def menu_keyboard():
    builder = ReplyKeyboardBuilder()

    builder.button(text="💎 Купить UC")
    builder.button(text="📦 Мои заказы")
    builder.button(text="🆘 Поддержка")

    builder.adjust(1)

    return builder.as_markup(
        resize_keyboard=True
    )


@dp.message(Command("start"))
async def start(message: Message):
    await message.answer(
        "🔥 Добро пожаловать в ZULMACH UC BOT!\n\n"
        "Пополнение PUBG Mobile UC быстро и удобно.",
        reply_markup=menu_keyboard()
    )


@dp.message()
async def menu(message: Message):

if message.text == "💎 Купить UC":

    text = "💎 Доступные пакеты UC:\n\n"

    for product in PRODUCTS:
        text += (
            f"🔹 {product['name']} — "
            f"{product['price']} ₽\n"
        )

    await message.answer(text)

    elif message.text == "📦 Мои заказы":
        await message.answer(
            "📦 У вас пока нет заказов."
        )

    elif message.text == "🆘 Поддержка":
        await message.answer(
            "🆘 Поддержка ZULMACH"
        )


async def main():
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
