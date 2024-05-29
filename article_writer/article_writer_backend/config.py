import os

API_KEY = os.getenv('API_KEY', 'be40bf82a06e4c958cee025b20ffb836')
AZURE_ENDPOINT = os.getenv('AZURE_ENDPOINT', 'https://rookie.openai.azure.com/')
API_VERSION = os.getenv('API_VERSION', '2023-06-01-preview')
LLM_CONFIG = {
    "api_key": API_KEY,
    "api_version": API_VERSION,
    "azure_endpoint": AZURE_ENDPOINT,
    "model": "rookie",
    "api_type": "azure"
}
