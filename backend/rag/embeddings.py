import requests
from config import HF_API_KEY

API_URL = "https://api-inference.huggingface.co/feature-extraction/all-MiniLM-L6-v2"

headers = {
    "Authorization": f"Bearer {HF_API_KEY}"
}

def get_embedding(text):

    response = requests.post(API_URL, headers=headers, json={"inputs": text})

    return response.json()