numbers = []

while True:
    user_input = input("Enter a number (or press Enter to quit): ")

    if user_input == "":
        break

    numbers.append(float(user_input))  # chuyển sang số

# Sắp xếp giảm dần
numbers.sort(reverse=True)

# Lấy 5 số lớn nhất (nếu không đủ thì lấy hết)
top_five = numbers[:5]

print("Top 5 greatest numbers:", top_five)