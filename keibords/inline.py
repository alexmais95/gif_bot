from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

in_kb = InlineKeyboardMarkup(
    inline_keyboard=[
        [
            InlineKeyboardButton(text='Telegram', url='tg://resolve?domain=AlexandrMais')
        ]
    ]
)
