def remove_odd(numbers):
    even_numbers = []

    for num in numbers:
        if num % 2 == 0:
            even_numbers.append(num)

    return even_numbers


def main():
    numbers = [1, 2, 3, 4, 5, 6, 7, 8]

    result = remove_odd(numbers)

    print("Original list:", numbers)
    print("List without odd numbers:", result)


main()