
# Medieval mass converter

# Input
talents = float(input("Enter talents:\n"))
pounds = float(input("\nEnter pounds:\n"))
lots = float(input("\nEnter lots:\n"))

# Constants
GRAMS_PER_LOT = 13.3
LOTS_PER_POUND = 32
POUNDS_PER_TALENT = 20

# Convert to grams
total_lots = lots + pounds * LOTS_PER_POUND + talents * POUNDS_PER_TALENT * LOTS_PER_POUND
total_grams = total_lots * GRAMS_PER_LOT

# Convert to kg + remaining grams
kilograms = int(total_grams // 1000)
grams = total_grams - kilograms * 1000

# Output
print("\nThe weight in modern units:")
print(f"{kilograms} kilograms and {grams:.2f} grams.")
