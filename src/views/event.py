from fastapi import APIRouter
from fastapi.responses import JSONResponse
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

    return JSONResponse(status_code=201, content=result)
