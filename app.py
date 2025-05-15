from flask import Flask, request
import os
import httpx

app = Flask(__name__)

# Render 환경 변수에서 읽어옵니다.
TELEGRAM_TOKEN = os.environ["TELEGRAM_TOKEN"]
CHAT_ID        = os.environ["CHAT_ID"]

def send_telegram_message(message):
    url = f"https://api.telegram.org/bot{TELEGRAM_TOKEN}/sendMessage"
    payload = {
        "chat_id": CHAT_ID,
        "text": message
    }
    headers = {
        "Content-Type": "application/json; charset=utf-8"
    }
    # httpx를 사용해 UTF-8로 정확히 전송
    with httpx.Client() as client:
        client.post(url, json=payload, headers=headers, timeout=10.0)

@app.route("/webhook", methods=["POST"])
def webhook():
    data = request.json or {}
    message = data.get("message", "📢 트레이딩뷰 알림 도착!")
    send_telegram_message(message)
    return "ok"

@app.route("/")
def home():
    return "✅ 서버 작동 중"

if __name__ == "__main__":
    # Render가 제공하는 PORT 환경변수를 우선 사용하고, 없으면 10000번 포트
    port = int(os.environ.get("PORT", 10000))
    app.run(host="0.0.0.0", port=port)

