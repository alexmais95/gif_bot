import asyncio
from aiogram import Bot, Dispatcher
from aiogram.enums import ParseMode
from settings.settings import TOKEN_BOT
from handlers import user_comand
from callback import callbackquery
from log_conf.log import BasicLog

b_log = BasicLog()
log = b_log.log_config()


async def main() -> None:
    bot = Bot(TOKEN_BOT, parse_mode=ParseMode.HTML)
    dp = Dispatcher()
    dp.include_routers(
        user_comand.router,
        callbackquery.router
    )
    log.info('Start work')
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())
