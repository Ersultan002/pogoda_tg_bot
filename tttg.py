from aiogram import Bot, Dispatcher, types
from aiogram.types import Message
import asyncio
import logging
token = '6691961430:AAFXTgKyiEHh0uvbyEkAwXuIAtdpYQ6cR34'


async def start_bot(bot: Bot):
    await bot.send_message(1049561651, text='Бот запущен!')


async def stop_bot(bot: Bot):
    await bot.send_message(1049561651, text='Бот остановлен!')


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b>Привет{message.from_user.first_name}.Рад тебя видет!</b>')
    await message.answer(f'<s>Привет{message.from_user.first_name}.Рад тебя видет!</s>')
    await message.reply(f'<tg-spoiler>Привет{message.from_user.first_name}.Рад тебя видет!</tg-spoiler>')
    

async def start():
    logging.basicConfig(level=logging.INFO,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%(lineno)d) - %(message)s"
                        )

async def start():
    bot=Bot(token=token, parse_mode='HTML')
    
    dp = Dispatcher()
    dp.startup.register(start_bot)
    dp.shutdown.register(stop_bot)



    dp.message.register(get_start)
    try:
        await dp.start_polling(bot)
    finally:
        await bot.session.close()

if __name__ == "__main__":
    asyncio.run(start())