import requests
from datetime import datetime
import os

APP_ID = os.environ["APP_ID"]
API_KEY = os.environ["API_KEY"]
HOST_DOMAIN = os.environ["HOST_DOMAIN"]
EXERCISE_ENDPOINT = os.environ["EXERCISE_ENDPOINT"]
TOKEN = os.environ["TOKEN"]
SHEETY_ENDPOINT = os.environ["SHEETY_ENDPOINT"]

headers_nutri = {
    "x-app-id": APP_ID,
    "x-app-key": API_KEY,
}

user_input = input("What did you do today? ")
parameters = {
    "query": user_input
}

response = requests.post(url=f"{HOST_DOMAIN}{EXERCISE_ENDPOINT}", json=parameters, headers=headers_nutri)
data = response.json()
print(data)

now = datetime.now()
date_str = now.strftime("%d/%m/%Y")
time_str = now.strftime("%H:%M:%S")

headers_sheety = {
    "Authorization": TOKEN
}
for exercise in data["exercises"]:
    activity = {
        "workout": {
            "date": date_str,
            "time": time_str,
            "exercise": exercise["user_input"],
            "duration": exercise["duration_min"],
            "calories": exercise["nf_calories"]
        }
    }
    response = requests.post(url=SHEETY_ENDPOINT, json=activity, headers=headers_sheety)
    data = response.json()
    print(data)
