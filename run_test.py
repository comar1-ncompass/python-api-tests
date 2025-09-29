import requests
import os
from dotenv import load_dotenv, set_key

load_dotenv()

def login():
    
    payload = {
        "username": os.getenv("USERNAME"),
        "password": os.getenv("PASSWORD")
    }
    
    response = requests.post(f"https://dev-api.n-compass.online/api/account/login", json=payload)
    
    response_body = response.json()
    
    set_key(".env", "API_TOKEN", new_token)
    
if __name__ == "__main__":
    login()