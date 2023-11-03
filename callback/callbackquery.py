from aiogram.types import CallbackQuery
from aiogram.exceptions import TelegramBadRequest
from contextlib import suppress
from aiogram import Router, F
from keibords.fabryks import Pagination, paginator
router = Router()


@router.callback_query(Pagination.filter(F.action.in_(['prev', 'next'])))
async def pagination_handler(call: CallbackQuery, callback_data: Pagination):
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
                reply_markup=paginator(page)
            )
        await call.answer()
    except IndexError:
        print('Out of range')
