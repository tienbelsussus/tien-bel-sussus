def remove_odd(numbers):
    even_list = []

    for num in numbers:
        if num % 2 == 0:  # kiểm tra số chẵn
            even_list.append(num)

    return even_list


# Main program
original_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]

new_list = remove_odd(original_list)

print("Original list:", original_list)
print("List without odd numbers:", new_list)