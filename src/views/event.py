import json

from fastapi import APIRouter, Response, status
from pydantic import BaseModel

from controllers.events import EventType, manage_event

router = APIRouter()


class EventBody(BaseModel):
    type: EventType
    amount: float
    origin: str = None
    destination: str = None


@router.post("/event")
async def event(body: EventBody):
    result = manage_event(body.type, body)

    if not result:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="0")

    return Response(status_code=status.HTTP_201_CREATED, content=json.dumps(result))
