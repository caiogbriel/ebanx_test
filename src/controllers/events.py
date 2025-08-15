from dataclasses import dataclass
from enum import Enum

from models.Account import AccountModel


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


def manage_event(
    type: EventType, event_data: DepositData | WithdrawData | TransferData
):
    if type == EventType.DEPOSIT:
        destination = event_data.destination
        amount = event_data.amount

        account = AccountModel.deposit(destination, amount)

        return {"destination": account.to_dict()}

    if type == EventType.WITHDRAW:
        origin = event_data.origin
        amount = event_data.amount

        account = AccountModel.get(origin)
        if not account:
            return None

        account.withdraw(amount)
        return {"origin": account.to_dict()}

    if type == EventType.TRANSFER:
        origin = event_data.origin
        destination = event_data.destination
        amount = event_data.amount

        origin_account = manage_event(
            EventType.WITHDRAW, WithdrawData(amount=amount, origin=origin)
        )

        if not origin_account:
            return None

        destination_account = manage_event(
            EventType.DEPOSIT, DepositData(amount=amount, destination=destination)
        )

        return {**origin_account, **destination_account}
