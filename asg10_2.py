import requests


def get_weather():
    city = input("Enter city: ")
    api_key = "223b1f5f2267dcdabd5648208b37707f"

    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}"

    try:
        response = requests.get(url)
        data = response.json()

        # kiểm tra lỗi từ API
        if data.get("cod") != 200:
            print("Error:", data.get("message"))
            return

        # lấy dữ liệu
        temp_kelvin = data["main"]["temp"]
        description = data["weather"][0]["description"]

        # chuyển Kelvin → Celsius
        temp_celsius = temp_kelvin - 273.15

        # in kết quả
        print("Weather:", description)
        print("Temperature:", round(temp_celsius, 2), "°C")

    except Exception as e:
        print("Something went wrong:", e)


get_weather()