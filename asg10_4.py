from flask import Flask, jsonify

app = Flask(__name__)


# hàm tìm airport theo ICAO
def find_airport(icao):
    with open("airports.csv", "r") as file:
        for line in file:
            code, name, city, country = line.strip().split(",")
            if code.upper() == icao.upper():
                return {
                    "icao": code,
                    "name": name,
                    "city": city,
                    "country": country
                }
    return None


# API endpoint
@app.route("/airport/<icao>")
def get_airport(icao):
    airport = find_airport(icao)

    if airport:
        return jsonify(airport)
    else:
        return jsonify({"error": "Airport not found"}), 404


# chạy server
if __name__ == "__main__":
    app.run(debug=True)