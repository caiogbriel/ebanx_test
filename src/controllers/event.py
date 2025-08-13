from enum import Enum


class EventType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"


def manage_event(type: EventType, event_data): ...
