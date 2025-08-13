from fastapi import FastAPI

from views.event import router as event_router

app = FastAPI()

app.include_router(event_router)
