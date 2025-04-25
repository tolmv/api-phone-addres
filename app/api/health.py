from fastapi import APIRouter, HTTPException
from app.models.schemas import HealthResponse
from app.services.phone_service import PhoneAddressService

router = APIRouter(tags=["health"])

@router.get("/health", response_model=HealthResponse)
async def health():
    """
    Health check redis connection endpoint.
    """
    is_healthy = await PhoneAddressService.check_health()
    
    if not is_healthy:
        raise HTTPException(status_code=503, detail="Redis connection failed")
        
    return {"status": "healthy", "redis": "connected"} 