from pydantic import BaseModel
from typing import Callable, Optional


class Command(BaseModel):
    name: str
    description: str
    handler: Callable

    class Config:
        arbitrary_types_allowed = True


class FromUser(BaseModel):
    id: int
    is_bot: bool
    first_name: Optional[str]
    username: Optional[str]


class Chat(BaseModel):
    id: int
    type: str
    title: Optional[str]


class Message(BaseModel):
    message_id: int
    from_: Optional[FromUser] = None
    chat: Chat
    date: int
    text: str

    class Config:
        fields = {
            "from_": "from"
        }


class Update(BaseModel):
    update_id: int
    message: Message
