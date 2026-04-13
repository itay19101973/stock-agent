from fastapi import FastAPI
from src.routes.webhook import bot_router
from src.repository.telegram import register_webhook_to_telegram
from src.repository.ngroc import get_ngroc_url

app = FastAPI()

app.include_router(bot_router)


@app.on_event("startup")
def startup():
    public_url = get_ngroc_url()

    if not public_url:
        print("❌ Could not get ngrok URL")
        return

    print("🌍 NGROK URL:", public_url)

    register_webhook_to_telegram(public_url)
    print("✅ Webhook registered!")