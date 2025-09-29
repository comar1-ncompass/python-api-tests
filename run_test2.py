import requests
import os
import time
from dotenv import load_dotenv
from helper.test_functions import (check_status_code, check_if_empty, check_response_time,
        check_no_auth_get                               
    )

load_dotenv()

def login_check():
    
    payload = {
        "username": os.getenv("TEST_USERNAME"),
        "password": os.getenv("TEST_PASSWORD")
    }
    
    response = requests.post(f"{os.getenv("BASE_URL")}/api/account/login", json=payload)
    # print(f"response: {response.json()}")
    print(f"test: {payload}")
    
    response_body = response.json()
    token = response_body.get('token')
    
    print(f"token: {token}")
    check_status_code(response.status_code)
    return token


def test_get_dealer_playlists(auth):
    
    payload = {
        "page" : 1,
        "dealerid" : os.getenv("TEST_DEALER_ID"),
        "search" : ""
    }
    
    headers = {
        "Authorization": f"Bearer {auth}"  # or just {auth} depending on your API
    }
    
    start_time = time.time()
    response = requests.get(f"{os.getenv("BASE_URL")}/api/playlists/getplaylistsbydealerid?", params=payload, headers=headers)
    
    print(f"response: {response.status_code}")
    print(f"test: {payload}")
    
    end_time = time.time()
    response_time = int((end_time - start_time) * 1000)  # C
    
    response_body = response.json()
    check_status_code(response.status_code)
    check_if_empty(response_body)
    check_response_time(response_time)
    check_no_auth_get("/api/playlists/getplaylistsbydealerid?", payload, headers)

def test_create_playlistv2(auth):
    
    payload = {
        "type": "unset",
        "assets": [],
        "playlistName": "Playlist2",
        "playlistDescription": "asdasd",
        "dealerId": "ff8c43b2-e894-43f1-bd39-6ce8323e910a"
    }
    
    headers = {
        "Authorization": f"Bearer {auth}"  # or just {auth} depending on your API
    }

    response = requests.get(f"{os.getenv("BASE_URL")}/api/playlistsv2", json=payload)
    
    print(f"response: {response.status_code}")
    print(f"test: {payload}")

if __name__ == "__main__":
    auth = login_check()
    
    test_get_dealer_playlists(auth)
    test_create_playlistv2(auth)