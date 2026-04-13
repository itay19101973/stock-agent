from fastapi import APIRouter, Request

from src.services.commands import COMMANDS
from src.routes.utils.webhook_utils import is_old_message

bot_router = APIRouter()


@bot_router.post("/webhook")
async def msg_handler(req: Request):
    """
    internal router to navigate between bot commands
    :param req:
    :return:
    """
    data = await req.json()

    message = data.get("message")
    if not message:
        return {"ok": True}

    if is_old_message(message):
        return {"ok": True}

    text = message.get("text", "")
    command = text.split()[0].lower()

    command_object = COMMANDS.get(command)
    handler = None
    if command_object:
        handler = command_object.handler

    if handler:
        handler(data)

    return {"ok": True}
