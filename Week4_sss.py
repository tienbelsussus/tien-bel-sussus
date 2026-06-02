# functional_pipeline.py

from specialized_housing import apartment, villa, penthouse
from specialized_housing import market_dashboard
from functools import reduce


print("\n========== DELIVERABLE 4.1 ==========")
print("BEST VALUE PROPERTIES")

# Step 1: Multi-Condition Filtering
best_value = list(
    filter(
        lambda prop: prop.price < 10.0 and prop.sqm > 60,
        market_dashboard
    )
)

for prop in best_value:
    prop.display_listing()


print("\n========== DELIVERABLE 4.2 ==========")
print("ANALYSIS LIST")

# Step 2: Complex Mapping
analysis_list = list(
    map(
        lambda prop:
        f"[ID: {prop.prop_id}] at {prop.address} | "
        f"Unit Price: {prop.price / prop.sqm:.4f}B per sqm",
        market_dashboard
    )
)

for item in analysis_list:
    print(item)


print("\n========== DELIVERABLE 4.3 ==========")
print("MARKET LEADER")

# Step 3: Advanced Reduce
market_leader = reduce(
    lambda p1, p2:
    p1 if p1.price > p2.price else p2,
    market_dashboard
)

print(
    f"Most expensive property:"
    f"\nID: {market_leader.prop_id}"
    f"\nAddress: {market_leader.address}"
    f"\nPrice: {market_leader.price}B VND"
)


print("\n========== DELIVERABLE 4.4 ==========")
print("SORTED BY SIZE")

# Step 4: Custom Sorting
sorted_by_size = sorted(
    market_dashboard,
    key=lambda prop: prop.sqm,
    reverse=True
)

for prop in sorted_by_size:
    print(
        f"ID: {prop.prop_id} | "
        f"{prop.address} | "
        f"{prop.sqm} sqm"
    )


print("\n========== DELIVERABLE 4.5 ==========")
print("CURRENCY CONVERTER")
# Step 5: Closures
def make_currency_converter(exchange_rate):

    def converter(price_bill_vnd):
        return (price_bill_vnd * 1_000_000_000) / exchange_rate

    return converter
to_usd = make_currency_converter(25000)
to_euro = make_currency_converter(27000)
penthouse_obj = next(
    filter(
        lambda prop: isinstance(prop, penthouse),
        market_dashboard
    )
)
print(
    f"Penthouse ID {penthouse_obj.prop_id}"
)
print(
    f"USD Value: "
    f"{to_usd(penthouse_obj.price):,.2f} USD"
)
print(
    f"EURO Value: "
    f"{to_euro(penthouse_obj.price):,.2f} EUR"
)


print("\n========== DELIVERABLE 4.6 ==========")
print("PROJECTED MARKET")

# Step 6: List Comprehension

projected_market = [
    {
        "ID": prop.prop_id,
        "Taxed_Price": round(prop.price * 1.1, 2)
    }
    for prop in market_dashboard
    if isinstance(prop, (apartment, penthouse))
]

for item in projected_market:
    print(item)


print("\n========== DELIVERABLE 4.7 ==========")
print("AUDIT TRACKER")
# Step 7: Decorator
def audit_log(func):
    def wrapper(*args, **kwargs):
        print(
            f"[LOG] Executing: "
            f"{func.__name__}..."
        )
        result = func(*args, **kwargs)
        print(
            f"[LOG] "
            f"{func.__name__} complete."
        )
        return result
    return wrapper
@audit_log
def update_listing_status(prop_id, status):
    print(
        f"Property {prop_id} "
        f"status updated to: {status}"
    )


update_listing_status(401, "SOLD")