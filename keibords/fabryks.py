from aiogram.types import InlineKeyboardButton
from aiogram.filters.callback_data import CallbackData
from aiogram.utils.keyboard import InlineKeyboardBuilder


class Pagination(CallbackData, prefix='relod'):
    action: str
    page: int


def paginator(page: int = 0):
    bilder = InlineKeyboardBuilder()
    bilder.row(
        InlineKeyboardButton(text='←', callback_data=Pagination(action='prev', page=page).pack()),
        InlineKeyboardButton(text='→', callback_data=Pagination(action='next', page=page).pack()),
        width=2

    )
    return bilder.as_markup()
