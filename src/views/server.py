from fastapi import APIRouter
from fastapi.responses import JSONResponse

from controllers.reset import reset_accounts

router = APIRouter()


@router.post("/reset")
async def reset():
    reset_accounts()
    return JSONResponse(status_code=200, content=0)
