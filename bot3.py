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
    print(message)
    #await bot.send_message(message.from_user.id,'Привет, у меня собраны решения подготовительных заданий ОГЭ и ЕГЭ по физике\nЧтобы начать, просто пришли мне формулировку задачи')
    mess = Assistant_bot()
    messa = mess.start
    print(type(messa))
    await bot.send_message(message.from_user.id,messa)






if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
