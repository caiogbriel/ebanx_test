import json

from fastapi import APIRouter, Response, status

from controllers.accounts import get_account_balance

router = APIRouter()


@router.get("/balance")
async def get_balance(account_id: str):
    balance = get_account_balance(account_id)

    if balance is None:
        return Response(status_code=status.HTTP_404_NOT_FOUND, content="0")

    return Response(
        status_code=status.HTTP_200_OK, content=json.dumps(balance)
    )
