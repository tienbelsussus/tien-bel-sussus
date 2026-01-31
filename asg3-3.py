smallest = None
largest = None

while True:
    s = input("Enter a number (press Enter to quit): ")

    if s == "":
        break

    num = float(s)

    if smallest is None or num < smallest:
        smallest = num

    if largest is None or num > largest:
        largest = num

if smallest is not None:
    print("Smallest number:", smallest)
    print("Largest number:", largest)
else:
    print("No numbers were entered.")
