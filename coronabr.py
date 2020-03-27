#!/usr/bin/env python3
# -*- coding: UTF-8 -*-

import requests
import os, sys
import json, telegram
from dotenv import load_dotenv

dir = os.path.dirname(os.path.abspath(__file__)) 
load_dotenv(dotenv_path="{}/ini.cfg".format(dir))

last = os.path.dirname(os.path.abspath(__file__)) 
load_dotenv(dotenv_path="{}/last.cfg".format(last))

tk_id = os.getenv("TOKENID")
chtid = os.getenv("CHAT_ID").split(',')
lastup = os.getenv("LASTUPDATE")

try:
    req = requests.get("https://thevirustracker.com/free-api?countryTotal=BR", headers={"User-Agent": "windows10"})
except:
    print('Problemas com acesso a página')
    exit()

dic = json.loads(req.text)
reg = (dic['countrydata'])

def checkupdate():
    for x in reg:
       return(x['total_active_cases'] + x['total_deaths'] + x['total_recovered'] + x['total_new_deaths_today'] + x['total_new_cases_today'])

def consulta():
    for x in reg:
       return(' 🇧🇷 ATUALIZAÇÃO CORONAVÍRUS 🇧🇷 \n\n' '☣ <b>Casos ativos:</b> '+ str(x['total_active_cases']) + '\n\n' '☠️ <b>Mortes:</b> '+ str(x['total_deaths']) + '\n\n' '🙏 <b>Recuperados:</b> '+ str(x['total_recovered']) + '\n\n'
       '☠️ <b>Mortos Hoje:</b> '+ str(x['total_new_deaths_today']) + '\n\n' '☣ <b>Novos casos Hoje:</b> '+ str(x['total_new_cases_today']) + '\n\n' )

def envioTelegram():
    bot = telegram.Bot(token=tk_id)
    try:
         for i in range(len(chtid)):
            bot.send_message(chat_id=chtid[i], text=consulta(), parse_mode='HTML')
    except telegram.TelegramError as erro:
        print(erro)  

def main():
    if int(checkupdate()) != int(lastup):
        text_file = open('last.cfg','w')
        text_file.write('LASTUPDATE=' + str(checkupdate()))
        envioTelegram()

if __name__ == '__main__':
        main()
