from pydantic import BaseModel

from controllers.interfaces.event import EventType


class EventBody(BaseModel):
    type: EventType
    amount: float
    origin: str = None
    destination: str = None
