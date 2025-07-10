from keep_alive import keep_alive
import json
import threading
import time
import requests

keep_alive()

def banner():
    print("=" * 50)
    print("🔥 TOOL SHARE BÀI VIẾT – LONGDZ TOOL (Render Ver)")
    print("📛 Tool by Longdz")
    print("🌐 fb.com/longdznhattraidatnay")
    print("=" * 50)

gome_token = []

def get_token(input_file):
    for cookie in input_file:
        header_ = {
            'cookie': cookie.strip(),
            'user-agent': 'Mozilla/5.0'
        }
        try:
            res = requests.get('https://business.facebook.com/content_management', headers=header_).text
            token = res.split('EAAG')[1].split('"')[0]
            gome_token.append(f'{cookie}|EAAG{token}')
        except Exception:
            continue
    return gome_token

def share(tach, id_share):
    cookie, token = tach.split('|')
    headers = {
        'cookie': cookie.strip(),
        'user-agent': 'Mozilla/5.0'
    }
    try:
        requests.post(
            f'https://graph.facebook.com/me/feed?link=https://m.facebook.com/{id_share}&published=0&access_token={token}',
            headers=headers
        )
    except Exception:
        pass

def run_tool():
    try:
        with open("config.json", "r") as f:
            config = json.load(f)

        with open(config["cookies_file"], "r") as f:
            input_file = [line.strip() for line in f if line.strip()]

        id_share = config["id_share"]
        delay = int(config["delay"])
        total_share = int(config["total_share"])
    except Exception as e:
        print("❌ Lỗi đọc config hoặc cookie:", e)
        return

    banner()
    all = get_token(input_file)
    stt = 0

    while stt < total_share:
        for tach in all:
            if stt >= total_share:
                break
            stt += 1
            threading.Thread(target=share, args=(tach, id_share)).start()
            print(f"[{stt}] ✅ SHARE THÀNH CÔNG ➤ ID: {id_share}")
            time.sleep(delay)

if __name__ == "__main__":
    run_tool()
