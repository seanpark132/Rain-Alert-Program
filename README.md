# Rain-Alert-Program

A program that checks the daily weather forecast and texts the user in the morning if it will rain at the location they input. 
Hourly weather data is pulled from OpenWeather Map's API (https://openweathermap.org/api) and the program checks if there will be any type of rainy weather 
in the next 12 hours. If the forecast has rainy weather, the program will text the user to bring an umbrella, by using the Twilio API. 

Before running the program, change "lat" and "long" in the .env.txt file to your location's latitude/longitude. You can find your latitude/longitude using https://www.latlong.net/. Also edit "MY_NUMBER" in the .env.txt file to your number, with the format: "+1{your number, no dashes}".
