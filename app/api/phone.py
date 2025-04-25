from fastapi import APIRouter
from app.models.schemas import WriteDataRequest, PhoneAddressResponse, StatusResponse
from app.services.phone_service import PhoneAddressService

router = APIRouter(tags=["phone-address"])

@router.get("/check_data", response_model=PhoneAddressResponse)
async def check_data(phone: str):
    """
    Get address by phone number.
    
    Args:
        phone: The phone number to look up
        
    Returns:
        The phone and address information
    """
    address = await PhoneAddressService.get_address_by_phone(phone)
    return {"phone": phone, "address": address}

@router.post("/write_data", response_model=StatusResponse)
async def write_data(data: WriteDataRequest):
    """
    Write or update address data for a phone number.
    
    Args:
        data: The phone and address data
        
    Returns:
        Status and the updated data
    """
    await PhoneAddressService.store_phone_address(data.phone, data.address)
    return {"status": "success", "phone": data.phone, "address": data.address} 