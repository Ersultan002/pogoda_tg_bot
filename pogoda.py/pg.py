import telebot
import requests
import json

bot = telebot.TeleBot('6494693163:AAGSdFQ0EVB1djDju71E92QsepGdq0A4faA')
API = '85061ce11363276e180d10ae742a516b'

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, 'Привет рад тебя видеть! Напиши название города')



@bot.message_handler(content_types=['text'])
def get_water(message):
    city = message.text.strip().lower()
    res = requests.get(f'https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API}&units=metric')
    if res.status_code == 200:  
        data = json.loads(res.text)
        temp = data["main"]["temp"]
        bot.reply_to(message, f'Сейчас погода: {temp}')

   # image = 'nosunny.png' if temp < 5.0 else "sunny.png"
   # file = open('./' + image, 'rb')
   # bot.send_photo(message.chat.id, file)
        
    else:
        bot.reply_to(message, f'Город указан не верно')



   

bot.polling(non_stop=True)