class Property:
    def __init__(self, prop_id, address, price_bill_vnd, sqm):
        if (prop_id > 0 and price_bill_vnd > 0 and sqm > 0):
            self.prop_id        = prop_id
            self.address        = address
            self.price_bill_vnd = price_bill_vnd
            self.sqm            = sqm
            print(f"--- System: [ID: {prop_id}] at {address} successfully constructed ---")
        else:
            print(f"--- Error: Invalid data for ID {prop_id} at {address}. Values must be positive. ---")

    def display_metrics(self):
        price_per_sqm = self.price_bill_vnd / self.sqm
        print(f"ID: {self.prop_id} | Listing: {self.address} | "
              f"Price: {price_per_sqm:.4f} Billion VND / sqm")

    def is_affordable(self, budget):
        return self.price_bill_vnd <= budget

    def update_price(self, new_price):
        self.price_bill_vnd = new_price
        print(f"--- System: ID {self.prop_id} price updated to {self.price_bill_vnd:.2f}B VND ---")

    def is_larger_than(self, other):
        return self.sqm > other.sqm
mock_database = [
    Property(103, "88 Tay Ho Rd",   12.0, 120),
    Property(104, "5 Nguyen Trai",   3.2,  50),
    Property(101, "12A Cau Giay St", 4.5,  65),
]
for prop in mock_database:
    new_price = round(prop.price_bill_vnd * 1.10, 2)
    prop.update_price(new_price)
mock_database[0].display_metrics()
tay_ho      = mock_database[0]
nguyen_trai = mock_database[1]
result = tay_ho.is_larger_than(nguyen_trai)
print(f"Is ID {tay_ho.prop_id} larger than ID {nguyen_trai.prop_id}? {result}")

property_a = Property(101, "12A Cau Giay St", 4.5, 65)
property_b = Property(102, "Unknown Alley", -1.0, 0)
property_a.display_metrics()
budget = 5.0
print("Affordable within 5.0B budget?:", property_a.is_affordable(budget))

target = mock_database[0]
print(type(target))
print(dir(target))
print(target.__dict__)