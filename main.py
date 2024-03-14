from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv
from database import bd as db
import asyncio
import os

load_dotenv()

from Commands.user_cmd import rp


bot = Bot(token = os.getenv("TOKEN_API"))
dp = Dispatcher()
dp.include_router(rp)
async def on_startup():
    await db.db_start()
    print("Бот запущен!!!")

async def main():
    dp.startup.register(on_startup)
    await bot.delete_webhook(drop_pending_updates = True)
    await dp.start_polling(bot)
    

if __name__ == "__main__":
    asyncio.run(main())