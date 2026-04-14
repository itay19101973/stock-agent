from src.services.telegram import reply_hi, reply_menu, reply_rita
from src.app_types.general import Command
from src.services.stocks import handle_get_stock_data


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
    "rita": Command(
        name="menu",
        description="",
        handler=reply_rita
    ),
    "stocks": Command(
        name="menu",
        description="for example 'stock snp' will return the data about snp index",
        handler=handle_get_stock_data
    ),
}
