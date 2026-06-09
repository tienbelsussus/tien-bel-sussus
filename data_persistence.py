import json
import csv
from specialized_housing import market_dashboard
# ==================================================
# CLASSES
# ==================================================
class Property:
    def __init__(self, prop_id, address, price, sqm):
        self.prop_id = prop_id
        self.address = address
        self.price = price
        self.sqm = sqm
class apartment(Property):
    pass
class villa(Property):
    pass
class penthouse(Property):
    pass
# ================================================
# DELIVERABLE 5.1
# JSON EXPORT
# ==================================================
def export_to_json(listings, filename):

    data = [
        {
            **listing.__dict__,
            "type": listing.__class__.__name__
        }
        for listing in listings
    ]

    with open(filename, "w", encoding="utf-8") as file:
        json.dump(data, file, indent=4)

    print(f"Data exported to {filename}")


# ==================================================
# DELIVERABLE 5.2
# JSON IMPORT (REHYDRATION)
# ==================================================

def import_from_json(filename):

    with open(filename, "r", encoding="utf-8") as file:
        data = json.load(file)
    imported_list = []
    for item in data:
        if item["type"] == "apartment":
            obj = apartment(
                item["prop_id"],
                item["address"],
                item["price"],
                item["sqm"]
            )
        elif item["type"] == "villa":

            obj = villa(
                item["prop_id"],
                item["address"],
                item["price"],
                item["sqm"]
            )
        elif item["type"] == "penthouse":
            obj = penthouse(
                item["prop_id"],
                item["address"],
                item["price"],
                item["sqm"]
            )

        imported_list.append(obj)

    return imported_list


# ==================================================
# DELIVERABLE 5.3
# CSV EXPORT
# ==================================================

def export_to_csv(listings, filename):

    header = [
        "id",
        "address",
        "price",
        "sqm",
        "type"
    ]

    with open(
        filename,
        "w",
        newline="",
        encoding="utf-8"
    ) as file:

        writer = csv.writer(file)

        writer.writerow(header)

        for listing in listings:

            writer.writerow([
                listing.prop_id,
                listing.address,
                listing.price,
                listing.sqm,
                listing.__class__.__name__
            ])

    print(f"CSV exported to {filename}")


# ==================================================
# DELIVERABLE 5.4
# INPUT VALIDATION
# ==================================================

def add_property(listings):

    while True:

        try:

            address = input(
                "Enter address: "
            )

            price = float(
                input(
                    "Enter price (Billion VND): "
                )
            )

            sqm = float(
                input(
                    "Enter area (sqm): "
                )
            )

            new_id = max(
                property.prop_id
                for property in listings
            ) + 1

            new_property = apartment(
                new_id,
                address,
                price,
                sqm
            )

            listings.append(new_property)

            print(
                "Property added successfully!"
            )

            break

        except ValueError:

            print(
                "Error: Price and area must be numbers."
            )


# ==================================================
# DELIVERABLE 5.5
# SYSTEM LOG
# ==================================================

def log_action(message):

    with open(
        "system.log",
        "a",
        encoding="utf-8"
    ) as file:

        file.write(message + "\n")


# ==================================================
# DELIVERABLE 5.6
# DATA INTEGRITY CHECK
# ==================================================

def verify_integrity(
        original_list,
        imported_list):

    if len(original_list) != len(imported_list):

        print("Data Integrity Failed")
        return

    for original, imported in zip(
            original_list,
            imported_list):

        if original.prop_id != imported.prop_id:

            print("Data Integrity Failed")
            return

    print("Data Integrity Verified")


# ==================================================
# RUN DELIVERABLE 5.1
# ==================================================

export_to_json(
    market_dashboard,
    "listings.json"
)

log_action(
    "Properties exported to JSON"
)


# ==================================================
# RUN DELIVERABLE 5.2
# ==================================================

loaded_data = import_from_json(
    "listings.json"
)

print("\nImported Object Types:")

for item in loaded_data:
    print(type(item))


# ==================================================
# RUN DELIVERABLE 5.3
# ==================================================

export_to_csv(
    market_dashboard,
    "market_report.csv"
)

log_action(
    "Properties exported to CSV"
)


# ==================================================
# RUN DELIVERABLE 5.6
# ==================================================

verify_integrity(
    market_dashboard,
    loaded_data
)


# ==================================================
# RUN DELIVERABLE 5.4
# UNCOMMENT TO TEST
# ==================================================
add_property(market_dashboard)
