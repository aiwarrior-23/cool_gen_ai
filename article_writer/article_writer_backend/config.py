import os

API_KEY = os.getenv('API_KEY', '<your-key>')
AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT', '<your-endpoint>')
API_VERSION = os.getenv('API_VERSION', '<your-api-version>')
LLM_CONFIG = {
    "api_key": API_KEY,
    "api_version": API_VERSION,
    "azure_endpoint": AZURE_ENDPOINT,
    "model": "<your-model>",
    "api_type": "azure"
}
