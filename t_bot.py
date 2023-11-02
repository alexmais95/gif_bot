import asyncio
from aiogram import Bot, Dispatcher, F, Router
from aiogram.enums import ParseMode
from aiogram.types import Message, CallbackQuery
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from API import Gif
from setting import TOKEN_BOT
import keibords
import media
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress

gif = Gif()

dp = Dispatcher()
router = Router()


class Form(StatesGroup):
    gif = State()


@dp.message(F.text.lower() == 'gif')
async def giff(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.gif)
    await message.answer('Какую гифку вы хотите?')


@dp.message(Form.gif)
async def get_gif(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    global list_id
    list_id = gif.get_gif(message.text)
    id_ = list_id[0].id
    await message.answer_document(f'https://media1.giphy.com/media/{id_}/200.gif', reply_markup=keibords.paginator())


@dp.callback_query(keibords.Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call: CallbackQuery, callback_data: keibords.Pagination):
    try:
        page_num = int(callback_data.page)
        page = page_num
        if callback_data.action == 'prev':
            if page_num > 0:
                page = page_num - 1
            else:
                page = page_num
        if callback_data.action == 'next':
            if page_num < 5:
                page = page_num + 1
            else:
                page = page_num

        id_ = list_id[page].id
        with suppress(TelegramBadRequest):
            await call.message.answer_document(
                f'https://media1.giphy.com/media/{id_}/200.gif',
                reply_markup=keibords.paginator(page)
            )
        await call.answer()
    except IndexError:
        print('Out of range')

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
    dp.include_router(router)
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
