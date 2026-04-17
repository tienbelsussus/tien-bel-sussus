def find_keyword_lines(filename, keyword):
    line_numbers = []

    with open(filename, "r") as file:
        for index, line in enumerate(file, start=1):
            if keyword in line:
                line_numbers.append(index)

    return line_numbers


print(find_keyword_lines("example.txt", "apple"))