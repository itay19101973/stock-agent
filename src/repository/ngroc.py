import time
import requests
from src.config import NGROK_API


def get_ngroc_url():
    time.sleep(5)

    for _ in range(10):
        try:
            data = requests.get(NGROK_API).json()
            tunnels = data.get("tunnels", [])

            if tunnels:
                return tunnels[0]["public_url"]

        except Exception:
            pass

        time.sleep(2)

    return None
