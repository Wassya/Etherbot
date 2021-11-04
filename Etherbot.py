import json

import requests
from aiogram import Bot, Dispatcher, types
from aiogram.types import CallbackQuery
from aiogram.utils import executor
from datetime import datetime

import Etherbotkeyboard as nav

TOKEN = "you_bot_token"

bot = Bot(token=TOKEN)
dp = Dispatcher(bot)




# стартовое сообщение
@dp.message_handler(commands="start")
async def cmd_start(message: types.Message):
    await message.reply("Привет, я могу показать твою статистику в Езермайне", reply_markup=nav.mainmenu)

# кнопка "Статистика"
@dp.callback_query_handler(text_contains="stata")
async def cmd_main(call: CallbackQuery):
    res = requests.get("https://api.ethermine.org/miner/you_wallet/currentstats")
    tojson = json.loads(res.text)
    data = tojson['data']
    # cur_stat=data['currentStatistics']
    timestamp = data['time']
    t_now = datetime.fromtimestamp(timestamp)
    timestamp = data['lastSeen']
    t_lastSeen = datetime.fromtimestamp(timestamp)

    bal = data['unpaid']
    balance = round((bal / (10 ** 18)), 4)
    usdm = data['usdPerMin']
    usdd = round((usdm * 1440), 2)

    hashrate = data['reportedHashrate']
    rep_hash = int(hashrate) / (10 ** 6)
    hashrate = data['currentHashrate']
    cur_hash = round(hashrate / (10 ** 6), 2)
    await call.message.answer(text=f'Хешрейт: {rep_hash}\nРеальный: {cur_hash}\nБалансEth: {balance}\nДоход в сутки$: {usdd}\nОнлайн: {t_lastSeen}', reply_markup=nav.mainmenu)

if __name__ == '__main__':
    executor.start_polling(dp)