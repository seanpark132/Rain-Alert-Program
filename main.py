import requests
from twilio.rest import Client
import os
from dotenv import load_dotenv

load_dotenv(".env.txt")
api_key = os.getenv("OMW_api_key")
lat = os.getenv("lat")
lon = os.getenv("lon")
account_sid = os.getenv("TWILIO_account_sid")
auth_token = os.getenv("TWILIO_auth_token")
MY_NUMBER = os.getenv("MY_NUMBER")

weather_params = {
    "lat": lat,
    "lon": lon,
    "appid": api_key,
    "exclude": "current,minutely,daily"
}

# pull weather data
response = requests.get(url="https://api.openweathermap.org/data/2.5/onecall", params=weather_params)
response.raise_for_status()
data = response.json()

bring_umbrella = False
for n in range(12):
    weather_id = int(data["hourly"][n]["weather"][0]["id"])
    if weather_id < 700:
        bring_umbrella = True
        break

if bring_umbrella:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body="It's going to rain today. Remember to bring a ☂️",
        from_="+12764448814",
        to=MY_NUMBER
    )
    print(message.status)
