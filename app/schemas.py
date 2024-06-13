from pydantic import BaseModel

class SMSSendRequest(BaseModel):
    to: str
    message: str

class SMSReceiveResponse(BaseModel):
    from_: str
    to: str
    body: str