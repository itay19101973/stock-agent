from src.services.telegram import reply_hi, reply_menu
from src.app_types.general import Command


COMMANDS = {
    "hi": Command(
        name="hi",
        description="replies hi to users",
        handler=reply_hi
    ),
    "menu": Command(
        name="menu",
        description="return list of commands",
        handler=reply_menu
    ),
}
