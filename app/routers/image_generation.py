from fastapi import APIRouter, HTTPException
from app.models.image_models import ImageGenerationRequest, ImageGenerationResponse
from app.services.replicate_service import generate_image

router = APIRouter()

@router.post("/generate-image", response_model=ImageGenerationResponse, summary="Generate Image")
async def generate_image_endpoint(request: ImageGenerationRequest):
    """Generate an image based on a text prompt using Replicate's API."""
    try:
        result = generate_image(request)
        return result
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
