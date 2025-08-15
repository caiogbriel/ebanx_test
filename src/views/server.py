from fastapi import APIRouter, Response, status

from controllers.accounts import reset_accounts

router = APIRouter()


@router.post("/reset")
async def reset():
    reset_accounts()

    return Response(status_code=status.HTTP_200_OK, content="OK")
