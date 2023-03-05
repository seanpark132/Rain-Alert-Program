# Rain-Alert-Program

A program that checks the daily weather forecast and texts the user in the morning if it will rain at the location they input. 
Hourly weather data is pulled from OpenWeather Map's API (https://openweathermap.org/api) and the program checks if there will be any type of rainy weather 
in the next 12 hours. If the forecast has rainy weather, the program will text the user to bring an umbrella, by using the Twilio API. 

Before running the program, several variables in the .env.txt file need to be changed:
* **lat**: user location's latitude
* **long**: user location's longitude
* **OMW_api_key**: OpenWeatherMap API key
* **TWILIO_account_sid**: Twilio  account SID
* **TWILIO_auth_token**: Twilio auth token
* **MY_NUMBER**: user's mobile phone number 
