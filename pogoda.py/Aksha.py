import telebot
from currency_converter import CurrencyConverter
from telebot import types

bot = telebot.TeleBot('6906757965:AAEghTu3C79JMgKNMNmMbzK0aWcylHz7AeI')
currency = CurrencyConverter()
amount = 0


@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Ассалаумағалейкум, сумма енгізіңіз !')
    bot.register_next_step_handler(message, summa)


def summa(message):
    global amount
    try:
       amount = int(message.text.strip())
    except ValueError:
        bot.send_message(message.chat.id, 'Тупойсынба сумма жазсай')
        bot.register_next_step_handler(message, summa)
        return

    if amount > 0:
       markup = types.InlineKeyboardMarkup(row_width=2)
       btn1 = types.InlineKeyboardButton('USD/EUR', callback_data='usd/eur')
       btn2 = types.InlineKeyboardButton('EUR/USD', callback_data='eur/usd')
       btn3 = types.InlineKeyboardButton('USD/GBP', callback_data='usd/gbp')
       btn4 = types.InlineKeyboardButton('Другое значение', callback_data='else')
       markup.add(btn1,btn2,btn3,btn4)
       bot.send_message(message.chat.id, 'Выберите пару валют', reply_markup=markup)
    else:
        bot.send_message(message.chat.id, '0 болмайды, қайта жаз')
        bot.register_next_step_handler(message, summa)
  

@bot.callback_query_handler(func=lambda call: True)
def callback(call):
    if call.data != 'else':
       values = call.data.upper().split('/')
       res = currency.convert(amount, values[0], values[1])
       bot.send_message(call.message.chat.id, f'Получается: {round(res,2)}. Можете занова вписать сумму')
       bot.register_next_step_handler(call.message, summa)
    else:
        bot.send_message(call.message.chat.id, 'Введите пару значений через слэш')
        bot.register_next_step_handler(call.message, summa, my_currency)
  

def my_currency(message):
    try:
        values = message.text.upper().split('/')
        res = currency.convert(amount, values[0], values[1])
        bot.send_message(message.chat.id, f'Получается: {round(res,2)}. Можете занова вписать сумму')
        bot.register_next_step_handler(message, summa)
    except Exception:
        bot.send_message(message.chat.id, f'Тупой дурыс жазсай')
        bot.register_next_step_handler(message, my_currency)

bot.polling(none_stop=True)