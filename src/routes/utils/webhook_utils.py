import time


def is_old_message(message: dict) -> bool:
    message_time = message.get("date", 0)
    now = int(time.time())

    return (now - message_time) > 60
