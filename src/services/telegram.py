from src.repository.telegram import send_message
from src.services.utils.telegram_utils import LIST_OF_COMMANDS
from src.app_types.general import Update


def reply_hi(data: Update):
    send_message(data.message.chat.id, "hi 👋")


def reply_menu(data: Update):
    send_message(data.message.chat.id, LIST_OF_COMMANDS)


def reply_rita(data: Update):
    send_message(data.message.chat.id, "She is the most bitch of all bitches that i know")
