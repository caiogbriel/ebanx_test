import json

from fastapi import APIRouter, Response, status

from controllers.event import manage_event
from views.interfaces.event import EventBody

router = APIRouter()


@router.post("/event")
async def event(body: EventBody):
    result = manage_event(body.type, body)

    if not result:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="0")

    return Response(status_code=status.HTTP_201_CREATED, content=json.dumps(result))
