from fastapi import APIRouter
from fastapi.responses import JSONResponse

from controllers.accounts import get_account_balance

router = APIRouter()


@router.get("/balance")
async def get_balance(account_id: str):
    balance = get_account_balance(account_id)

    if balance is None:
        return JSONResponse(status_code=404, content=0)

    return JSONResponse(status_code=200, content=balance)
