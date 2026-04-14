from src.app_types.general import Update
from src.repository.stocks import get_stock_data
from src.repository.telegram import send_message

INDEX_MAP = {
    "snp": "SPY",
    "snp500": "SPY",
    "spx": "SPY",
    "s&p500": "SPY",
    "sp500": "SPY",
    "nasdaq": "QQQ",
    "dow": "DIA"
}


def handle_get_stock_data(update: Update):
    text = update.message.text or ""
    parts = text.split()

    if len(parts) < 2:
        send_message(update.message.chat.id, "Usage: stocks <symbol1> <symbol2> ...")
        return

    user_inputs = parts[1:]

    resolved_symbols = []
    failed_symbols = []

    for symbol in user_inputs:
        mapped = INDEX_MAP.get(symbol.lower(), symbol.upper())

        if not mapped:
            failed_symbols.append(symbol)
        else:
            resolved_symbols.append(mapped)

    if not resolved_symbols:
        send_message(update.message.chat.id, "No valid symbols provided.")
        return

    data = get_stock_data(resolved_symbols)

    if data is None:
        send_message(update.message.chat.id, "Error fetching stock data.")
        return

    response_lines = []

    for quote in data.data:
        line = f"{quote.ticker}: {quote.price}"

        if quote.day_high and quote.day_low:
            line += f" (Daily High: {quote.day_high} / Daily Low: {quote.day_low})"

        response_lines.append(line)

    if failed_symbols:
        response_lines.append(f"\nUnknown: {', '.join(failed_symbols)}")

    final_message = "\n".join(response_lines)

    send_message(update.message.chat.id, final_message)



