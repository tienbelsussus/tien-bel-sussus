cities = []

# Nhập 5 thành phố
for i in range(5):
    city = input(f"Enter city {i+1}: ")
    cities.append(city)

# In ra từng thành phố
print("\nList of cities:")
for city in cities:
    print(city)