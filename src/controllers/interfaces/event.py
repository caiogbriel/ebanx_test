from dataclasses import dataclass
from enum import Enum


class EventType(Enum):
    DEPOSIT = "deposit"
    WITHDRAW = "withdraw"
    TRANSFER = "transfer"


@dataclass
class DepositData:
    amount: float
    destination: str


@dataclass
class WithdrawData:
    amount: float
    origin: str


@dataclass
class TransferData:
    amount: float
    origin: str
    destination: str
