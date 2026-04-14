import requests
from pydantic import ValidationError

from src.app_types.stocks import StockQuoteResponse
from src.config import stock_data_api_key

base_stocks_url = "https://api.stockdata.org"


def get_stock_data(stock_symbols: list[str]) -> StockQuoteResponse | None:
    url = base_stocks_url + "/v1/data/quote"

    params = {
        "symbols": ",".join(stock_symbols),
        "api_token": stock_data_api_key
    }

    try:
        response = requests.get(url, params=params, timeout=5)
    except requests.RequestException:
        return None

    if response.status_code != 200:
        return None

    try:
        data = StockQuoteResponse(**response.json())
    except ValidationError:
        return None

    if not data.data:
        return None

    return data
