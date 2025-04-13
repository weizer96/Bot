import asyncio
from aiogram import Bot, Dispatcher
from config import load_config
from handlers import start, services, date_time, contact

config = load_config()
bot = Bot(token=config.bot_token)
dp = Dispatcher()

dp.include_router(start.router)
dp.include_router(services.router)
dp.include_router(date_time.router)
dp.include_router(contact.router)

async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
