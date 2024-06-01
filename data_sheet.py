import requests
import pandas as pd

GOOGLE_SHEET_NAME = "sheet1"
USER_NAME = "soroushak84"
PASSWORD = "Sa1384"
google_sheet_endpoint_post = "https://api.sheety.co/264aeabc6ddf3801a77aa09b5a1dac08/accounting/sheet1"
df = pd.read_json("data.json")


data_dict = df.to_dict()
key_list = list(data_dict.keys())

sheet_inputs_list = []

def send_to_google():
    for key in data_dict:
        account_data = data_dict[key]
        # if key == "admin":
        #     continue
        sheet_inputs = {
            GOOGLE_SHEET_NAME: {
                "username" : key,
                "email" : account_data["email"],
                "fname" : account_data["fname"],
                "lname" : account_data["lname"],
                "password" : account_data["password"]
            }
        }
        sheet_inputs_list.append(sheet_inputs)
        
    for sheet_inputs in sheet_inputs_list:
        sheet_response = requests.post(
            google_sheet_endpoint_post,
            json=sheet_inputs,
            auth=(
                USER_NAME,
                PASSWORD,
            )
        )


    print(f"Sheety Response: \n {sheet_response.text}")

send_to_google()