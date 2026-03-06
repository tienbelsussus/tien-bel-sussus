seasons = ("winter", "spring", "summer", "autumn")

month = int(input("Enter the number of a month (1-12): "))

season_index = (month % 12) // 3

print("Season:", seasons[season_index])