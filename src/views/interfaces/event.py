from typing import Optional

from pydantic import BaseModel

from controllers.interfaces.event import EventType


class EventBody(BaseModel):
    type: EventType
    amount: float
    origin: Optional[str] = None
    destination: Optional[str] = None
