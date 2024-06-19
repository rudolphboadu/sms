from pydantic import BaseModel

class SMSSendRequest(BaseModel):
    to_phone_number: str
    message: str

class SMSReceiveResponse(BaseModel):
    from_: str
    to_phone_number: str
    body: str