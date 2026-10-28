import asyncio
import os
from aiogram import Bot, Dispatcher, types
from dotenv import load_dotenv

# Загружаем секреты
load_dotenv()

BOT_TOKEN = os.getenv("TELEGRAM_BOT_TOKEN")

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

@dp.message()
async def handle_message(message: types.Message):
    await message.answer("Привет! Я бот для генерации видео. Скоро я научусь это делать!")

async def main():
    print("Бот запущен!")
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
