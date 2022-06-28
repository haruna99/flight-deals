import os
from twilio.rest import Client
import smtplib

SMTP_DOMAIN = "smtp.mail.yahoo.com"
MY_EMAIL = "haruna99.test@yahoo.com"
PASSWORD = os.environ.get("YAHOO_PASSWORD")

account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']


class NotificationManager:

    def __init__(self, flight_data):
        self.flight_data = flight_data
        self.client = Client(account_sid, auth_token)

        # self.send_text()

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

    def send_emails(self, email):
        flight_link = f"https://www.google.com/travel/flights?q=Flights%20to" \
                      f"%20{self.flight_data.to_city_airport}%20from%20" \
                      f"{self.flight_data.from_city_airport}%20on%20{self.flight_data.travel_date}" \
                      f"%20through%20{self.flight_data.return_date}"
        with smtplib.SMTP(SMTP_DOMAIN) as connection:
            connection.starttls()
            connection.login(user=MY_EMAIL, password=PASSWORD)
            connection.sendmail(
                from_addr=MY_EMAIL,
                to_addrs=email,
                msg=f"Subject:New Low Price Alert!\n\nLow Price Alert! Only £{self.flight_data.price} to fly from "
                    f"{self.flight_data.from_city}-{self.flight_data.from_city_airport} to "
                    f"{self.flight_data.to_city}-{self.flight_data.to_city_airport}, from "
                    f"{self.flight_data.travel_date} to {self.flight_data.return_date}"
                    f"\n{flight_link}".encode('utf-8')
            )
