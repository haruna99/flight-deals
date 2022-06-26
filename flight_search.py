import requests
import datetime as dt
from pprint import pprint
from flight_data import FlightData

API_KEY = "ifiIKN2agrURLyNyVkmtq1fsFEbE3wFm"
API_ID = "harunaogwedaflightsearch"
API_URL = "https://tequila-api.kiwi.com/"
API_KEY = "ifiIKN2agrURLyNyVkmtq1fsFEbE3wFm"

headers = {
    "apikey": API_KEY
}


class FlightSearch:
    def __init__(self):
        pass

    def search_for_flight_code(self, city):
        parameters = {
            "term": city,
            "location_types": "city"
        }
        response = requests.get(url=f"{API_URL}locations/query", headers=headers, params=parameters)
        response.raise_for_status()
        locations = response.json()["locations"]
        return locations[0]["code"]

    def search_for_flight(self, from_city, to_city):
        today = dt.date.today()
        date_from = today + dt.timedelta(days=1)
        date_to = today + dt.timedelta(days=180)
        parameters = {
            "fly_from": from_city,
            "fly_to": to_city,
            "date_from": date_from.strftime("%d/%m/%Y"),
            "date_to": date_to.strftime("%d/%m/%Y"),
            "nights_in_dst_from": 7,
            "nights_in_dst_to": 28,
            "flight_type": "round",
            "curr": "GBP",
            "one_for_city": 1,
            "max_stopovers": 0
        }
        response = requests.get(url=f"{API_URL}v2/search", headers=headers, params=parameters)
        response.raise_for_status()
        try:
            data = response.json()["data"][0]
            flight_data = FlightData(
                price=data["price"],
                to_city=data["cityTo"],
                from_city=data["cityFrom"],
                from_city_airport=data["route"][0]["flyFrom"],
                to_city_airport=data["route"][0]["flyTo"],
                travel_date=data["route"][0]["local_departure"].split("T")[0],
                return_date=data["route"][1]["local_departure"].split("T")[0]
            )
            pprint(f"{flight_data.to_city}: £ {flight_data.price}")
            return flight_data
        except IndexError:
            print(f"No flights found for {to_city}.")
            return None
