numbers = []

while True:
    user_input = input("Enter a number (press Enter to quit): ")

    if user_input == "":
        break

    number = float(user_input)
    numbers.append(number)

# sort numbers in descending order
numbers.sort(reverse=True)

# get the five greatest numbers
top_five = numbers[:5]

print("The five greatest numbers are:")
for num in top_five:
    print(num)