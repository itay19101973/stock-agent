import os

TOKEN = os.getenv("TELEGRAM_TOKEN")
NGROK_API = os.getenv("NGROK_API")

if not TOKEN:
    raise ValueError("TELEGRAM_TOKEN is missing")

TELEGRAM_API = f"https://api.telegram.org/bot{TOKEN}"

chat_id = os.getenv("CHAT_ID")
stock_data_api_key = os.getenv("STOCK_DATA_API_KEY")

DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")

DATABASE_URL = (
    f"postgresql://{DB_USER}:{DB_PASSWORD}"
    f"@{DB_HOST}:{DB_PORT}/{DB_NAME}"
)
