from data_manager import DataManager
from flight_search import FlightSearch
from notification_manager import NotificationManager

data_manager = DataManager()
sheet_data = data_manager.prices

flight_search = FlightSearch()

for city in sheet_data:
    if not city["iataCode"]:
        response = flight_search.search_for_flight_code(city["city"])
        object_id = city["id"]
        data_manager.update_sheet_data(response, object_id)

    search_for_flight = flight_search.search_for_flight("LON", city["iataCode"])

    try:
        if search_for_flight.price <= city["lowestPrice"]:
            notification_manager = NotificationManager(
                flight_data=search_for_flight
            )
    except AttributeError as message:
        print(message)
