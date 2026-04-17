import requests

api_key = "223b1f5f2267dcdabd5648208b37707f"
city = input("Enter municipality name: ")

geo_url = f"http://api.openweathermap.org/geo/1.0/direct?q={city}&limit=1&appid={api_key}"
geo_response = requests.get(geo_url)
geo_data = geo_response.json()

if geo_data:
    lat = geo_data[0]["lat"]
    lon = geo_data[0]["lon"]

    weather_url = "https://api.openweathermap.org/data/2.5/weather"
    params = {
        "lat": lat,
        "lon": lon,
        "appid": api_key,
        "units": "metric"
    }

    weather_response = requests.get(weather_url, params=params)
    weather_data = weather_response.json()

    description = weather_data["weather"][0]["description"]
    temperature = weather_data["main"]["temp"]

    print("Weather:", description)
    print("Temperature:", temperature, "°C")

else:
    print("City not found")
