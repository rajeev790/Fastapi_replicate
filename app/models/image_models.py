from pydantic import BaseModel

class ImageGenerationRequest(BaseModel):
    prompt: str
    model: str = "default"  # Default model version

class ImageGenerationResponse(BaseModel):
    image_url: str
