import os
import requests
from dotenv import load_dotenv

load_dotenv()

def check_status_code(code): #code: int
    if code == 200 or code == 201:
        print("status code test passed")
        return True
    else:
        print("status code test failed")
        return False
    
def check_if_empty(response_body): #playlists: []
    playlists = response_body.get("playlists")
    if not playlists:
        print("JSON is empty")
        return True
    else:
        print("JSON is not empty")
        return False
    
def check_response_time(response_time):
    # Performance classification
    if response_time <= 500:
        print("Fast")
    elif response_time <= 2500:
        print("Medium")
    elif response_time <= 5000:
        print("Slow")
    else:
        print("Very Slow")
    
    # return result

def check_no_auth_get(request, payload, headers): #request: string
    response = requests.get(f"{os.getenv("BASE_URL")}{request}", params=payload, headers=headers)
    if response.status_code != 200:
        print("Test Passes")
    else:
        print("Test Fails")
        