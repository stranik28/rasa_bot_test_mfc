import requests

url = 'http://rasa:5005/webhooks/rest/webhook'

async def send_message(message, user):
    res = requests.post(url, json={"message":message, "sender":str(user)})

    # print(res.text)\
    if res.status_code == 200:
        return res.json().pop().get('text')
    else:
        return "Error with status code" + str(res.status_code)
    
# Simple aiogram bot
import aiogram
from aiogram import Bot, Dispatcher, types

import logging
logging.basicConfig(level=logging.INFO)

tocken = '530896196:AAFisuSZ19_h_8s7jE5K7coXwzjH5PPZwKg'
bot = Bot(token=tocken)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def process_start_command(message: types.Message):
    await message.reply("Hi! I'm TestNLP bot!\nPowered by aiogram.")

@dp.message_handler(commands=['help'])
async def process_help_command(message: types.Message):
    await message.reply("Help!")

@dp.message_handler()
async def echo_message(msg: types.Message):
    await msg.reply(await send_message(msg.text, msg.from_user.id))

if __name__ == '__main__':
    from aiogram import executor
    executor.start_polling(dp, skip_updates=True)