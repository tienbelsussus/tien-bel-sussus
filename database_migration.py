import sqlite3
import json
import pandas as pd

DB_FILE = "housing_market.db"

def migrate_data(filepath):

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    with open(filepath, "r", encoding="utf-8") as f:
        data = json.load(f)

    for item in data:
        cursor.execute("""
        INSERT OR IGNORE INTO listings
        (prop_id,address,price,sqm,property_type)
        VALUES (?,?,?,?,?)
        """,
        (
            item["prop_id"],
            item["address"],
            item["price"],
            item["sqm"],
            item["property_type"]
        ))

    conn.commit()
    conn.close()


def verify_migration():

    conn = sqlite3.connect(DB_FILE)
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM listings")

    count = cursor.fetchone()[0]

    print("Total Rows:", count)

    cursor.execute("SELECT * FROM listings LIMIT 5")

    rows = cursor.fetchall()

    print("\nFirst 5 Records")

    for row in rows:
        print(row)

    conn.close()

conn=sqlite3.connect(DB_FILE)

df=pd.read_sql_query(
    "SELECT * FROM listings",
    conn,
    index_col="prop_id"
)

print(df.head())

print(f"\nTotal listings: {len(df)}")

if not df.empty:

    avg_price=df.groupby("property_type")["price"].mean()

    print("\nAverage Price")

    print(avg_price)
df_villas=pd.read_sql_query(
"""
SELECT *
FROM listings
WHERE property_type='villa'
AND price>6
""",
conn,
index_col="prop_id"
)

print(df_villas.head())

conn.close()
migrate_data("scraped_data.json")
verify_migration()