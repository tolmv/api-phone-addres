from fastapi import HTTPException
from app.database import redis_client

class PhoneAddressService:
    @staticmethod
    async def get_address_by_phone(phone: str) -> str:
        """
        Get address by phone number.
        
        Args:
            phone: The phone number to look up
            
        Returns:
            The address associated with the phone number
            
        Raises:
            HTTPException: If phone number is not found
        """
        if not phone:
            raise HTTPException(status_code=400, detail="Phone number is required")
        
        address = redis_client.get(phone)
        if not address:
            raise HTTPException(status_code=404, detail="Phone number not found")
            
        return address
        
    @staticmethod
    async def store_phone_address(phone: str, address: str) -> None:
        """
        Store or update a phone-address pair.
        
        Args:
            phone: The phone number
            address: The address to store
            
        Raises:
            HTTPException: If validation fails
        """
        if not phone or not address:
            raise HTTPException(status_code=400, detail="Both phone and address are required")
            
        redis_client.set(phone, address)
        
    @staticmethod
    async def check_health() -> bool:
        """
        Check if Redis connection is healthy.
        
        """
        try:
            return redis_client.ping()
        except Exception:
            return False