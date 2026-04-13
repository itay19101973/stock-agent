import requests

from src.config import TELEGRAM_API


def register_webhook_to_telegram(public_url: str):
    current = requests.get(f"{TELEGRAM_API}/getWebhookInfo").json()

    if current.get("result", {}).get("url") == f"{public_url}/webhook":
        print("Webhook already set, skipping")
        return

    requests.post(f"{TELEGRAM_API}/setWebhook", json={
        "url": f"{public_url}/webhook"
    })


def send_message(chat_id: str, text: str):
    requests.post(f"{TELEGRAM_API}/sendMessage", json={
        "chat_id": chat_id,
        "text": text
    })
