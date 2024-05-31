import pandas as pd

def start():
    df = pd.read_json('cities.json')
    city_names = df["name"].astype(str).tolist()
    return city_names

#print(start())
