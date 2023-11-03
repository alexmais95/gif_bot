from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from API.Gif_api import Gif
from aiogram import F, Router
from keibords import inline, reply, fabryks
from media.media_loder import muz

router = Router()
gif = Gif()


class Form(StatesGroup):
    gif = State()


class Giflist:
    l_st: list


@router.message(F.text.lower() == 'gif')
async def giff(message: Message, state: FSMContext) -> None:
    await state.set_state(Form.gif)
    await message.answer('Какую гифку вы хотите?')


@router.message(Form.gif)
async def get_gif(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    list_id = gif.get_gif(message.text)
    Giflist.l_st = list_id
    id_ = list_id[0].id
    await message.answer_document(f'https://media1.giphy.com/media/{id_}/200.gif', reply_markup=fabryks.paginator())


@router.message(F.text.lower() == 'nasa')
async def start(message: Message) -> None:
    await message.answer(f'your massage{message}', reply_markup=reply.main_kb)


@router.message(F.text.lower() == 'audio')
async def start(message: Message) -> None:
    await message.answer_audio(audio=muz, reply_markup=reply.main_kb)


@router.message()
async def text(message: Message) -> None:
    msg = message.text.lower()

    if msg == 'link':
        await message.answer('Telegram_autor_url:', reply_markup=inline.in_kb)
