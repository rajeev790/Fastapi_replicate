# Replicate Image Generation API

## Overview

This FastAPI application provides an API for generating images based on text prompts using the Replicate API. The service takes in a text prompt, sends it to the Replicate API, and returns the generated image's URL.

## Features

- **Image Generation**: Generate an image based on a text prompt using Replicate's models.
- **Modular Structure**: Clean, maintainable code structure with separate modules for routing, services, and models.
- **Environment Configuration**: Securely manage API keys using environment variables.
- **Documentation**: Self-documented API accessible via Swagger UI.


## Getting Started

### Prerequisites

- **Python**: Make sure Python 3.8+ is installed.
- **Replicate API Key**: Sign up at [Replicate](https://replicate.com/) to obtain an API key.

### Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/fastapi_replicate.git
    cd fastapi_replicate
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install Dependencies**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
   Create a `.env` file in the root directory and add your Replicate API key:
    ```plaintext
    REPLICATE_API_KEY="your_replicate_api_key"
    ```

### Running the Application

Start the FastAPI application with Uvicorn:

```bash
uvicorn app.main:app --reload
