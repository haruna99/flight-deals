import requests

API_URL = "https://api.sheety.co/75b910ec42643eafc84fedae1ff65ac8/flightDeals/prices"
API_KEY = "tftrf7636^$vuyghuhi2i2guuiyuguuyu"
headers = {
    "Authorization": f"Bearer {API_KEY}"
}


class DataManager:
    def __init__(self):
        self.data = ""
        self.prices = ""
        self.get_sheet_data()

    def get_sheet_data(self):
        response = requests.get(url=API_URL, headers=headers)
        self.data = response.json()
        self.prices = self.data["prices"]

    def update_sheet_data(self, response, object_id):
        payload = {
            "price": {
                "iataCode": response
            }
        }
        response = requests.put(url=f"{API_URL}/{object_id}", headers=headers, json=payload)
        self.data = response.json()

