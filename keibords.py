from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

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