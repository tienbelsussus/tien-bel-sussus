import requests
import json

icao = input("Enter the ICAO code of the airport: ")

url = f"http://127.0.0.1:5000/airport/{icao}"
response = requests.get(url).json()

print(json.dumps(response, indent=2))