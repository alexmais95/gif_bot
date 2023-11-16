from aiogram.types import Message
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from API.Gif_api import Gif
from aiogram import F, Router
from keibords import inline, reply, fabryks
from media.media_loder import muz
from sql.db import DataBase
from datetime import date
from log_conf.log import BasicLog

router = Router()
gif = Gif()
db = DataBase()
b_log = BasicLog()
log = b_log.log_config()


class Form(StatesGroup):
    gif = State()


class StartForm(StatesGroup):
    year = State()


class Giflist:
    l_st: list


@router.message(F.text.lower() == 'start')
async def giff(message: Message, state: FSMContext) -> None:
    await state.set_state(StartForm.year)
    log.info('Write inf in db about user')
    await message.answer(f'Hello {message.from_user.first_name} {message.from_user.last_name},'
                         f'write your date of birth like this: 1995-9-15')


@router.message(StartForm.year)
async def write_in_db(message: Message, state: FSMContext) -> None:
    await state.update_data(name=message.text)
    b_day = message.text.split(sep='-')
    try:
        db.add_users_data(message.from_user.first_name, message.from_user.last_name,
                          date(int(b_day[0]), int(b_day[1]), int(b_day[2])))
    except Exception as ex:
        print(f'Some mistake: {ex}')
        log.info(ex)
    finally:
        await message.answer('Good job.)')
        await state.clear()


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
    log.info('request for make gif')
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
