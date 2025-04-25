from pydantic import BaseModel, Field

class WriteDataRequest(BaseModel):
    phone: str = Field(...)
    address: str = Field(...)

class PhoneAddressResponse(BaseModel):
    phone: str = Field(...)
    address: str = Field(...)

class StatusResponse(BaseModel):
    status: str = Field(...)
    phone: str = Field(...)
    address: str = Field(...)

class HealthResponse(BaseModel):
    status: str = Field(...)
    redis: str = Field(...) 