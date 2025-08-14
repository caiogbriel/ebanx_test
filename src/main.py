from fastapi import FastAPI

from views.event import router as event_router
from views.server import router as server_router

app = FastAPI()

app.include_router(event_router, prefix="/v1")
app.include_router(server_router, prefix="/v1")
