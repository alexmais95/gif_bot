import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.enums import ParseMode
from aiogram.types import Message
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from API import Gif
from setting import TOKEN_BOT
import keibords
import media

dp = Dispatcher()
router = Router()
dp.include_router(router)
gif = Gif()


class Form(StatesGroup):
    gif = State()


@router.message(F.text.lower() == 'gif')
async def giff(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.gif)
    await message.answer('Какую гифку вы хотите?')


@router.message(Form.gif)
async def get_gif(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    id_ = gif.get_gif(message.text)
    await message.answer_document(f'https://media1.giphy.com/media/{id_}/200.gif')


@dp.message(F.text.lower() == 'nasa')
async def start(message: Message) -> None:
    await message.answer(f'your massage{message}', reply_markup=keibords.main_kb)


@dp.message(F.text.lower() == 'audio')
async def start(message: Message) -> None:
    await message.answer_audio(audio=media.muz, reply_markup=keibords.main_kb)

@dp.message()
async def text(message: Message) -> None:
    msg = message.text.lower()

    if msg == 'link':
        await message.answer('Telegram_autor_url:', reply_markup=keibords.in_kb)



async def main() -> None:
    bot = Bot(TOKEN_BOT, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
