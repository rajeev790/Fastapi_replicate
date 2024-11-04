from fastapi import FastAPI
from app.routers import image_generation

app = FastAPI(
    title="Replicate Image Generation API",
    description="An API to generate images based on a text prompt using Replicate.",
    version="1.0.0",
)

# Register the router for image generation
app.include_router(image_generation.router, prefix="/api/v1")
