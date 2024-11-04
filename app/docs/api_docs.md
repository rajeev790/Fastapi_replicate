# Replicate Image Generation API Documentation

### Base URL
`/api/v1`

### Endpoints

#### `POST /generate-image`

Generates an image based on a given text prompt.

**Request Body:**
- `prompt` (string): The text prompt for image generation.
- `model` (string, optional): The model version for generation. Defaults to "default".

**Response:**
- `image_url` (string): URL to the generated image.

Example Request:
```json
{
  "prompt": "A beautiful sunset over the mountains",
  "model": "default"
}
{
  "image_url": "https://replicate.com/output/sample.jpg"
}
