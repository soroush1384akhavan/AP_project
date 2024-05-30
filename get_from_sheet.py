import requests
import pandas as pd
import json

GOOGLE_SHEET_NAME = "workout"
USER_NAME = "soroush1384akhavan"
PASSWORD = "sa1384"
google_sheet_endpoint_post = "https://api.sheety.co/bd9514ce5c9d48ad46feff3f53f91a6e/copyOfMyWorkouts/workouts"

def get_from_google():
    response = requests.get(google_sheet_endpoint_post, auth=(USER_NAME, PASSWORD))
    data = response.json()
    return data
    with open("credentials.json", "w") as file:
        json.dump(data, file)
    for account in data["workouts"]:
        if account["username"] == "admin" :
            print(account)

get_from_google()