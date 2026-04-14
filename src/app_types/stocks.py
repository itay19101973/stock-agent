from pydantic import BaseModel
from typing import List, Optional


class StockQuote(BaseModel):
    ticker: str
    price: float
    day_high: Optional[float] = None
    day_low: Optional[float] = None
    volume: Optional[int] = None


class StockQuoteResponse(BaseModel):
    data: List[StockQuote]
