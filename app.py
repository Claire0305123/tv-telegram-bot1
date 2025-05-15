from flask import Flask, request
import requests

import os

app = Flask(__name__)

TELEGRAM_TOKEN = os.environ.get("TELEGRAM_TOKEN")
CHAT_ID = os.environ.get("CHAT_ID")

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    requests.post(url, json=payload)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json
    message = data.get("message", "📢 트레이딩뷰 알림 도착!")
    send_telegram_message(message)
    return "ok"

@app.route("/")
def home():
    return "✅ 서버 작동 중"

app.run(host="0.0.0.0", port=10000)
