import asyncio

from aiogram import Bot, Dispatcher, types
import configg

bot= Bot(configg.BOT_TOKEN)
dp = Dispatcher()


@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    await bot.send_invoice(message.chat.id, 'Покупка курса','Покупка курсак itProger','invoice', configg.PAYMENT_TOKEN, 'KZT', [types.LabeledPrice('Покупка курса', 5000*100)])

asyncio.run(start())