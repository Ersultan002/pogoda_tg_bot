from aiogram import Bot
from aiogram.types import Message


async def get_start(message: Message, bot: Bot):
    await bot.send_message(message.from_user.id, f'<b>Привет{message.from_user.first_name}.Рад тебя видет!</b>')
    await message.answer(f'<s>Привет{message.from_user.first_name}.Рад тебя видет!</s>')
    await message.reply(f'<tg-spoiler>Привет{message.from_user.first_name}.Рад тебя видет!</tg-spoiler>')