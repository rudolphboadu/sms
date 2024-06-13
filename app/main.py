from fastapi import FastAPI, HTTPException, Request, Depends
from twilio.rest import Client
from twilio.twiml.messaging_response import MessagingResponse
from .schemas import SMSSendRequest, SMSReceiveResponse
from .config import settings

app = FastAPI()

client = Client(settings.twilio_account_sid, settings.twilio_auth_token)


@app.get("/")
async def root():
    return {"message": "Hello World"}

@app.post("/send-sms/")
async def send_sms(sms_request: SMSSendRequest):
    try:
        message = client.messages.create(
            body=sms_request.message,
            from_=settings.twilio_phone_number,
            to=sms_request.to
        )
        return {"sid": message.sid, "status": message.status}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

@app.post("/receive-sms/")
async def receive_sms(request: Request):
    form_data = await request.form()
    response = MessagingResponse()
    response.message("Thank you for your message!")

    return {
        "from": form_data.get("From"),
        "to": form_data.get("To"),
        "body": form_data.get("Body")
    }