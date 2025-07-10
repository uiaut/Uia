from keep_alive import keep_alive
import json
import threading
import time
import requests
import os
from pystyle import Colorate, Colors

keep_alive()

def banner():
    print(Colorate.Horizontal(Colors.blue_to_cyan, """
   _____ __                       _    _____
  / ___// /_  ____ _________     | |  / <  /
  \__ \/ __ \/ __ `/ ___/ _ \    | | / // / 
 ___/ / / / / /_/ / /  /  __/    | |/ // /  
/____/_/ /_/\__,_/_/   \___/     |___//_/   
"""))

gome_token = []

def get_token(input_file):
    for cookie in input_file:
        header_ = {
            'cookie': cookie,
            'user-agent': 'Mozilla/5.0'
        }
        try:
            res = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = res.split('EAAG')[1].split('"')[0]
            gome_token.append(f'{cookie}|EAAG{token}')
        except:
            pass
    return gome_token

def share(tach, id_share):
    cookie, token = tach.split('|')
    headers = {
        'cookie': cookie,
        'user-agent': 'Mozilla/5.0'
    }
    try:
        requests.post(
            f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}',
            headers=headers
        )
    except:
        pass

def run_tool():
    with open("config.json", "r") as f:
        config = json.load(f)

    input_file = open(config["cookies_file"]).read().split('\n')
    id_share = config["id_share"]
    delay = int(config["delay"])
    total_share = int(config["total_share"])

    banner()
    all = get_token(input_file)
    stt = 0

    while stt < total_share:
        for tach in all:
            stt += 1
            threading.Thread(target=share, args=(tach, id_share)).start()
            print(f"[{stt}] SHARE ➤ THÀNH CÔNG ➤ ID {id_share}")
            time.sleep(delay)
            if stt >= total_share:
                break

run_tool()
