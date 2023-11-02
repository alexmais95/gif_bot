from aiogram.types import (
    ReplyKeyboardMarkup,
    KeyboardButton,
    InlineKeyboardMarkup,
    InlineKeyboardButton
)
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pagination(CallbackData, prefix='relod'):
    action: str
    page: int



def paginator(page: int = 0):
    bilder = InlineKeyboardBuilder()
    bilder.row(
        InlineKeyboardButton(text='←', callback_data=Pagination(action='prev', page=page, text='text').pack()),
        InlineKeyboardButton(text='→', callback_data=Pagination(action='next', page=page, text='text').pack()),
        width=2

    )
    return bilder.as_markup()


main_kb = ReplyKeyboardMarkup(
    keyboard=[
        [
            KeyboardButton(text='Gif'),
            KeyboardButton(text='Audio')
        ],
        [KeyboardButton(text='Nasa')]
    ],
    resize_keyboard=True,
    one_time_keyboard=True,
    input_field_placeholder='Chuse one params',
    selective=True
)

in_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=AlexandrMais')
        ]
    ]
)
