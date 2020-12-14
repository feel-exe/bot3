# Грузим библиотеки
import aiogram
from aiogram import Bot, Dispatcher, executor, types

from helper import Assistant_bot

# Грузим из файлов
from config import TOKEN

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)  # кусок от aiogram



@dp.message_handler(commands=["start"])
async def process_start_command(message: types.Message):
    await bot.send_message(message.from_user.id,Assistant_bot().start())

@dp.message_handler(commands=["help"])
async def process_help_command(message: types.Message):
    await bot.send_message(message.from_user.id, Assistant_bot().help())

@dp.message_handler(commands=["donations"])
async def process_donations_command(message: types.Message):
    await bot.send_message(message.from_user.id, "Тут можно поддержать проект", parse_mode="Markdown")




if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
