
from src.config import NGROK_API
import requests
import time


def get_ngrok_url():
    time.sleep(5)

    for _ in range(10):
        try:
            response = requests.get(NGROK_API, timeout=3)
            response.raise_for_status()

            data = response.json()

            tunnels = data.get("tunnels", [])
            if tunnels:
                return tunnels[0].get("public_url")

        except requests.exceptions.RequestException as e:
            print(f"[ngrok] network error: {e}")

        except ValueError as e:
            print(f"[ngrok] JSON parse error: {e}")

        time.sleep(2)

    return None
