import requests
import pandas as pd
import json

GOOGLE_SHEET_NAME = "sheet1"
USER_NAME = "soroushak84"
PASSWORD = "Sa1384"
google_sheet_endpoint_post = "https://api.sheety.co/084b9ab5553470a6b6b23e99b2506c1c/accounting/sheet1"

def get_from_google():
    response = requests.get(google_sheet_endpoint_post, auth=(USER_NAME, PASSWORD))
    data = response.json()
    #print(data)
    return data
    with open("credentials.json", "w") as file:
        json.dump(data, file)
    for account in data["workouts"]:
        if account["username"] == "admin" :
            print(account)

if __name__ == "__main__":
    get_from_google()