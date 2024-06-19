from fastapi import FastAPI
from app.routers import sms

app = FastAPI(title="PyCommsPay SMS",
    description="",
    summary="",
    version="0.0.1",)

app.include_router(sms.router)


