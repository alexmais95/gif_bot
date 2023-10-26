import asyncio
from aiogram import Bot, Dispatcher, Router, types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart
from aiogram.types import Message
from API import Gif
from setting import TOKEN


TOKEN = TOKEN
dp = Dispatcher()
gif = Gif()



@dp.message()
async def start(message: types.Message) -> None:
    await message.answer(gif.get_gif(message.text))


async def main() -> None:
    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
