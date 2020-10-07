from fastapi import APIRouter
from datetime import datetime
from app.models import (
    RequestMeterRead,
    ResponseMeterRead,
)
from app.grpc_client import search

router = APIRouter()


@router.post(
    "/query",
    name="meter:query",
    response_model=ResponseMeterRead,
)
async def fetch(timeline: RequestMeterRead):
    print(timeline.start)
    return search(timeline.start, timeline.limit, timeline.precision)
    # return {"labels": ["a", "b", "c"], "data": [5, 2, 1]}
