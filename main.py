import asyncio
from aiogram import Bot, Dispatcher, types
from aiogram.filters import CommandStart # type: ignore

bot = Bot(token="6260661732:AAHMffiLkBZ_e6gv0IBcdvi1i5W7WnwcWoE")
dp = Dispatcher()


@dp.message(CommandStart())
async def start_cmd(message: types.Message):
    await message.answer('Это была команда старт')


@dp.message()
async def echo(message: types.Message):

    await message.answer(message.text)
    await message.reply(message.text)


async def main():
    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)

asyncio.run(main())