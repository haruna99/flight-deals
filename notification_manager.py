import os
from twilio.rest import Client

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


class NotificationManager:

    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.client = Client(account_sid, auth_token)

        self.send_text()

    def send_text(self):
        self.client.messages \
            .create(
                body=f"Low Price Alert! Only £{self.flight_data.price} to "
                     f"fly from {self.flight_data.from_city}-{self.flight_data.from_city_airport} "
                     f"to {self.flight_data.to_city}-{self.flight_data.to_city_airport}, "
                     f"from {self.flight_data.travel_date} to {self.flight_data.return_date}",
                from_=os.environ['TWILIO_FROM_NUMBER'],
                to=os.environ['TWILIO_TO_NUMBER']
            )
