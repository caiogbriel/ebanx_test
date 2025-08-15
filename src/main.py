from fastapi import FastAPI

from views.balance import router as balance_router
from views.event import router as event_router
from views.server import router as server_router

app = FastAPI()

app.include_router(balance_router)
app.include_router(event_router)
app.include_router(server_router)
