import pandas as pd

import matplotlib.pyplot as plt


def ingest_and_inspect_data(filepath='scraped_data.json'):
    """
    Step 1: DataFrame Ingestion & Inspection
    Loads scraped data into a DataFrame, sets index, and prints info.
    """
    print(f"\n--- Step 1: DataFrame Ingestion & Inspection ({filepath}) ---")

    try:
        # Load the scraped data into a Pandas DataFrame
        df = pd.read_json(filepath)
        print(f"Successfully loaded {filepath}\n")
    except ValueError:
        # Fallback in case you decide to use CSV instead
        df = pd.read_csv(filepath)
        print(f"Successfully loaded {filepath} as CSV\n")
    except FileNotFoundError:
        print(f"Error: {filepath} not found. Have you run the scraper yet?")
        return None

    # Set the unique id (prop_id) as the index of the DataFrame
    if 'prop_id' in df.columns:
        df.set_index('prop_id', inplace=True)
    elif 'ID' in df.columns:
        df.set_index('ID', inplace=True)

    # View the first 5 rows
    print("--- First 5 Rows (df.head()) ---")
    print(df.head())
    print("\n" + "=" * 60 + "\n")

    # Verify the data types
    print("--- DataFrame Info (df.info()) ---")
    df.info()
    print("============================================================\n")

    return df


def feature_engineering(df):
    """
    Step 2: Feature Engineering (Calculated Columns)
    Adds unit_price_mil and market_segment columns to the DataFrame.
    """
    print("\n--- Step 2: Feature Engineering ---")

    # Task 1: Calculate unit_price_mil (Convert Billions to Millions, then divide by sqm)
    df['unit_price_mil'] = (df['price'] * 1000) / df['sqm']

    # Task 2: Create market_segment using a custom function and .apply()
    def segment_property(price):
        if price < 3.0:
            return "Value"
        elif price <= 10.0:  # Covers 3.0 to 10.0
            return "Standard"
        else:
            return "Premium"

    # Apply the function to the price column
    df['market_segment'] = df['price'].apply(segment_property)

    # Note: Depending on your scraper, your location column might be named
    # 'address', 'title', or 'location'. We will safely check for 'address' or 'title'.
    col_name = 'address' if 'address' in df.columns else 'title'

    # Verify the results
    print(f"\n--- Verifying Engineered Columns (First 10 Rows) ---")
    print(df[[col_name, 'unit_price_mil', 'market_segment']].head(10))
    print("============================================================\n")

    return df


def market_descriptive_statistics(df):
    """
    Step 3: Market Descriptive Statistics
    Generates summary stats, finds the most expensive property per sqm,
    and calculates total market value.
    """
    print("\n--- Step 3: Market Descriptive Statistics ---")

    # Task 1: Generate a full statistical summary of numerical columns
    print("\n--- Statistical Summary (.describe()) ---")
    # We select only the relevant numerical columns to keep the output clean
    stats_summary = df[['price', 'sqm', 'unit_price_mil']].describe()
    print(stats_summary)

    # Task 2: Find the specific property with the highest unit_price_mil
    # .idxmax() gets the index (prop_id) of the highest value
    max_unit_price_idx = df['unit_price_mil'].idxmax()

    # .loc[] grabs the entire row for that specific index
    most_expensive_prop = df.loc[max_unit_price_idx]

    # Safely get the address (handling potential column naming differences from scrapers)
    col_name = 'address' if 'address' in df.columns else 'title'
    highest_address = most_expensive_prop[col_name]
    highest_unit_price = most_expensive_prop['unit_price_mil']

    print("\n--- Highest Unit Price Property ---")
    print(f"Property ID: {max_unit_price_idx}")
    print(f"Address/Title: {highest_address}")
    print(f"Unit Price: {highest_unit_price:.2f} Million VND/sqm")
    print(f"Total Price: {most_expensive_prop['price']} Billion VND")

    # Task 3: Calculate the Total Market Value
    total_market_value = df['price'].sum()

    print("\n--- Total Market Value ---")
    print(f"The total value of all scraped properties is: {total_market_value:.2f} Billion VND")
    print("============================================================\n")

    return df

def grouping_and_segmentation(df):
    """
    Step 4: Grouping and Segmentation Analysis
    Groups by property type to find averages/counts, and filters for premium large homes.
    """
    print("\n--- Step 4: Grouping and Segmentation Analysis ---")

    # Task 1: Group by Property Type (e.g., Apartment, Villa, Penthouse)
    # Note: Depending on your Week 6 scraper, this column might be named 'type', 'property_type', or 'category'.
    # We will check for 'property_type' or 'type'.
    col_type = 'property_type' if 'property_type' in df.columns else 'type'


    if col_type in df.columns:
        # Group by the type, then calculate both mean and count
        grouped_stats = df.groupby(col_type).agg(
            avg_unit_price_mil=('unit_price_mil', 'mean'),
            total_listings=(col_type, 'count')
        )

        # Sort so the most expensive category (by unit price) is at the top
        grouped_stats = grouped_stats.sort_values(by='avg_unit_price_mil', ascending=False)

        print(f"\n--- Market Summary by Category ---")
        print(grouped_stats)
    else:
        print(f"\nWarning: Could not find a property type column to group by.")
        print(f"Available columns are: {list(df.columns)}")

    # Task 2: Filter for Premium Large Homes
    # We use the & operator to combine two conditions. Make sure to wrap each condition in parentheses!
    premium_large_homes = df[(df['market_segment'] == 'Premium') & (df['sqm'] > 100)]

    print("\n--- Premium Large Homes (>100 sqm) ---")
    print(f"Total matching properties found: {len(premium_large_homes)}")

    # Safely get the title/address column for the printout
    col_name = 'address' if 'address' in df.columns else 'title'

    # Display the first few results of our filtered subset
    if not premium_large_homes.empty:
        print(premium_large_homes[[col_name, 'sqm', 'price', 'unit_price_mil']].head())
    else:
        print("No properties in the dataset matched both criteria.")

    print("============================================================\n")

    return df


def visualizing_market_trends(df):
    """
    Step 5: Visualizing Market Trends
    Generates and saves a Bar Chart (market segments) and a Scatter Plot (sqm vs price).
    """
    print("\n--- Step 5: Visualizing Market Trends ---")

    # Check if we have the necessary columns before plotting
    if 'market_segment' not in df.columns or 'sqm' not in df.columns or 'price' not in df.columns:
        print("Error: Missing required columns for plotting. Ensure Steps 1 and 2 ran correctly.")
        return df

    # Task 1: Create a Bar Chart for market_segment
    print("Generating Bar Chart: segment_bar.png...")
    plt.figure(figsize=(8, 6))  # Set the figure size

    # Calculate counts and plot
    segment_counts = df['market_segment'].value_counts()
    segment_counts.plot(kind='bar', color=['#4C72B0', '#55A868', '#C44E52'])

    # Add titles and labels
    plt.title('Total Properties by Market Segment')
    plt.xlabel('Market Segment')
    plt.ylabel('Number of Properties')
    plt.xticks(rotation=0)  # Keeps the segment names horizontal

    # Save the plot and clear the canvas
    plt.tight_layout()
    plt.savefig('segment_bar.png')
    plt.close()  # CRITICAL: Close the plot so it doesn't overlap with the next one!

    # Task 2: Create a Scatter Plot for sqm vs price
    print("Generating Scatter Plot: sqm_price_scatter.png...")
    plt.figure(figsize=(10, 6))

    # Create the scatter plot
    df.plot.scatter(x='sqm', y='price', alpha=0.7, color='purple')

    # Add titles and labels
    plt.title('Property Size (sqm) vs. Price (Billion VND)')
    plt.xlabel('Area (Square Meters)')
    plt.ylabel('Price (Billion VND)')

    # Save the plot and clear the canvas
    plt.tight_layout()
    plt.savefig('sqm_price_scatter.png')
    plt.close()

    print("Success! Both plots have been saved to your project folder.")
    print("============================================================\n")

    return df


def run_market_analysis():
    # Step 1: Ingest and Inspect
    df = ingest_and_inspect_data('scraped_data.json')

    if df is not None:
        # Step 2: Feature Engineering
        df = feature_engineering(df)

        # Step 3: Descriptive Statistics
        df = market_descriptive_statistics(df)

        # Step 4: Grouping and Segmentation Analysis
        df = grouping_and_segmentation(df)

        # Step 5: Visualizing Market Trends
        df = visualizing_market_trends(df)
    return df

run_market_analysis()