import requests

# We need coordinates to get weather data
latitude = 48.85   # Paris latitude
longitude = 2.35   # Paris longitude

# Build the API URL with our parameters
url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"

# Make the request
response = requests.get(url)
data = response.json()

print(data)

data.keys()
data["current"]  # current weather data
data["current"]["temperature_2m"]  # current temperature in Celsius

def get_weather(latitude, longitude):
    url = f"https://api.open-meteo.com/v1/forecast?latitude={latitude}&longitude={longitude}&current=temperature_2m"
    response = requests.get(url)
    data = response.json()
    return data["current"]["temperature_2m"]

paris_temp = get_weather(48.85, 2.35)
print(f"The current temperature in Paris is {paris_temp}°C")
london_temp = get_weather(51.51, -0.13)
print(f"The current temperature in London is {london_temp}°C")

"""
The pattern of api call is:
1. you send request to a specific URL with parameters
2. api process and give you find the data
3. convert the data into a format you can use (like json)
4. extract the specific information you need from the data

"""