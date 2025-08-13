from fastapi import APIRouter
from fastapi.responses import JSONResponse
from pydantic import BaseModel

from controllers.event import EventType, manage_event

router = APIRouter()


class EventBody(BaseModel):
    type: EventType
    amount: float
    origin: str = None
    destination: str = None


@router.post("/event")
async def event(body: EventBody):
    event_data = body.model_dump()
    event_type = event_data.pop("type")

    result = manage_event(event_type, event_data)

    return JSONResponse(status_code=201, content=result)
