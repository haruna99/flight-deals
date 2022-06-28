import requests
import os
API_URL = "https://api.sheety.co/75b910ec42643eafc84fedae1ff65ac8/flightDeals/"
API_KEY = os.environ.get("SHEETY_API_KEY")
headers = {
    "Authorization": f"Bearer {API_KEY}"
}


class DataManager:
    def __init__(self):
        self.data = ""
        self.prices = ""
        self.get_sheet_data()
        self.users_data = ""
        self.users = ""
        self.get_users_data()

    def get_sheet_data(self):
        response = requests.get(url=f"{API_URL}/prices", headers=headers)
        self.data = response.json()
        self.prices = self.data["prices"]

    def update_sheet_data(self, response, object_id):
        payload = {
            "price": {
                "iataCode": response
            }
        }
        response = requests.put(url=f"{API_URL}/prices/{object_id}", headers=headers, json=payload)
        self.data = response.json()

    def get_users_data(self):
        response = requests.get(url=f"{API_URL}/users", headers=headers)
        self.users_data = response.json()
        self.users = self.users_data["users"]

