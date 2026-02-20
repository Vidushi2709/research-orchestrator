import os
from dotenv import load_dotenv
import requests

load_dotenv()

api_key = os.getenv("MISTRAL_API_KEY")

headers = {
    "Authorization": f"Bearer {api_key}",
    "Content-Type": "application/json"
}

# Simple test call
data = {
    "model": "mistral-small-latest",
    "messages": [{"role": "user", "content": "Hello"}],
    "max_tokens": 10
}

response = requests.post(
    "https://api.mistral.ai/v1/chat/completions",
    headers=headers,
    json=data
)

print(f"Status Code: {response.status_code}")
print(f"Response: {response.json()}")