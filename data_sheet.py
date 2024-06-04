import requests
import pandas as pd

GOOGLE_SHEET_NAME = "sheet1"
USER_NAME = "soroushak84"
PASSWORD = "Sa1384"
google_sheet_endpoint_post = "https://api.sheety.co/084b9ab5553470a6b6b23e99b2506c1c/accounting/sheet1"

try:
    df = pd.read_json("data.json")
except ValueError as e:
    print(f"Error reading JSON file: {e}")
    exit(1)

data_dict = df.to_dict()
# print(data_dict)
key_list = list(data_dict.keys())

sheet_inputs_list = []

def send_to_google():
    for key in data_dict:
        account_data = data_dict[key]
    
        required_fields = ["email", "password", "fname", "lname", "phonenumber", "city", "birthday", "securitytext"]
        if not all(field in account_data for field in required_fields):
            print(f"Missing fields for user {key}: {account_data}")
            continue
        if key == "admin":
            continue
        
        sheet_inputs = {
            GOOGLE_SHEET_NAME: {
                "username": key,
                "email": account_data["email"],
                "fname": account_data["fname"],
                "lname": account_data["lname"],
                "password": account_data["password"],
                "phonenumber": account_data["phonenumber"],
                "city": account_data["city"],
                "birthday": account_data["birthday"],
                "securitytext": account_data["securitytext"]
            }
        }
        sheet_inputs_list.append(sheet_inputs)

    for sheet_inputs in sheet_inputs_list:
        try:
            sheet_response = requests.post(
                google_sheet_endpoint_post,
                json=sheet_inputs,
                auth=(
                    USER_NAME,
                    PASSWORD,
                )
            )
            sheet_response.raise_for_status() 
        except requests.exceptions.RequestException as e:
            print(f"Request failed: {e}")
            continue

        print(f"Sheety Response for {sheet_inputs[GOOGLE_SHEET_NAME]['username']}: \n {sheet_response.text}")

#send_to_google()
