import requests

url = "https://alonhadat.com.vn/can-ban-nha-dat/ha-noi"

headers = {
    "User-Agent": "Mozilla/5.0"
}

response = requests.get(url, headers=headers)

if response.status_code != 200:
    print("Error: Cannot connect to website!")
else:
    print("--- Connection Successful: Data Received ---")

from bs4 import BeautifulSoup

soup = BeautifulSoup(response.text, "html.parser")

items = soup.find_all("a")

count = 0

for item in items:

    text = item.get_text(strip=True)

    if len(text) > 30:

        print("Property", count+1)
        print(text)
        print("----------------")

        count += 1

    if count == 3:
        break

def clean_price(text):

    try:

        text = text.replace("tỷ", "")
        text = text.replace("triệu", "")
        text = text.strip()

        return float(text)

    except:

        return None
def clean_area(text):

    try:

        text = text.replace("m²", "")
        text = text.replace("m2", "")

        return int(float(text.strip()))

    except:

        return None
raw_price = "5.5 tỷ"

raw_area = "75 m²"

print("Raw Price:", raw_price)

print("Clean Price:", clean_price(raw_price))

print()

print("Raw Area:", raw_area)

print("Clean Area:", clean_area(raw_area))

class Property:

    def __init__(self, prop_id, address, price, sqm):

        self.id = prop_id

        self.address = address

        self.price = price

        self.sqm = sqm
scraped_results = []

prop_id = 5001


for i in range(3):

    p = Property(

        prop_id,

        f"Property {i+1}",

        5.5 + i,

        75 + i*10

    )

    scraped_results.append(p)

    prop_id += 1
print("Total objects created:")
print(len(scraped_results))

import json
data = []
for p in scraped_results:
    data.append(p.__dict__)
with open(
    "scraped_data.json",
    "w",
    encoding="utf-8"
) as file:

    json.dump(
        data,
        file,
        indent=4
    )

print("JSON saved!")

import csv
with open(
    "scraped_data.csv",
    "w",
    newline=""
) as file:
    writer = csv.writer(file)
    writer.writerow(
        ["id","address","price","sqm"]
    )
    for p in scraped_results:

        writer.writerow([
            p.id,
            p.address,
            p.price,
            p.sqm
        ])
print("CSV saved!")