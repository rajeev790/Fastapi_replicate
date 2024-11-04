import requests
from app.config import settings
from app.models.image_models import ImageGenerationRequest, ImageGenerationResponse

def generate_image(request: ImageGenerationRequest) -> ImageGenerationResponse:
    url = "https://api.replicate.com/v1/predictions"
    headers = {
        "Authorization": f"Token {settings.replicate_api_key}",
        "Content-Type": "application/json",
    }
    payload = {
        "version": request.model,
        "input": {"prompt": request.prompt}
    }

    response = requests.post(url, json=payload, headers=headers)
    response.raise_for_status()
    data = response.json()

    # Extract the image URL from the response
    image_url = data.get("output", {}).get("url", "")
    return ImageGenerationResponse(image_url=image_url)
