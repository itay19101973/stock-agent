from fastapi import APIRouter, Request
from pydantic import ValidationError

from src.services.commands import COMMANDS
from src.routes.utils.webhook_utils import is_old_message
from src.app_types.general import Update

bot_router = APIRouter()


@bot_router.post("/webhook")
async def msg_handler(req: Request):
    data = await req.json()

    try:
        update = Update(**data)
    except ValidationError:
        return {"ok": True}  # ignore invalid payloads safely

    message = update.message
    if not message:
        return {"ok": True}

    if is_old_message(message.dict()):
        return {"ok": True}

    text = message.text or ""
    if not text:
        return {"ok": True}

    command = text.split()[0].lower()

    command_object = COMMANDS.get(command)
    if not command_object:
        return {"ok": True}

    handler = command_object.handler

    if handler:
        # pass structured data instead of raw dict
        handler(update)

    return {"ok": True}