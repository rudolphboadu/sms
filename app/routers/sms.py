from fastapi import APIRouter, Depends
from fastapi import FastAPI, HTTPException, Request, Depends
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from app.schemas import SMSSendRequest, SMSReceiveResponse
from app.config import settings

router = APIRouter(
    prefix="/Routes",
    tags=["routes"],
)

client = Client(settings.twilio_account_sid, settings.twilio_auth_token)


@router.get("/")
async def init():
    return {"message": "PyCommsPay SMS Init"}

@router.post("/send-sms/")
async def send_sms(sms_request: SMSSendRequest):
    try:
        message = client.messages.create(
            body=sms_request.message,
            from_=settings.twilio_phone_number,
            to=sms_request.to_phone_number
        )
        return {"sid": message.sid, "status": message.status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
