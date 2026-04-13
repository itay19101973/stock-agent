import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
NGROK_API = os.getenv("NGROK_API")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN is missing")

TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

chat_id = os.getenv("CHAT_ID")
