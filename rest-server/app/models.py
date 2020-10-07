from pydantic import BaseModel
from typing import Sequence, Optional
from datetime import datetime


class RequestMeterRead(BaseModel):
    start: datetime
    limit: int = 10
    precision: str = "15m"


class ResponseMeterRead(BaseModel):
    labels: Sequence[datetime]
    data: Sequence[float]
    message: str
