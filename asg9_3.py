def convert_to_uppercase(filename):
    with open(filename, "r") as file:
        content = file.read()

    content = content.upper()

    with open("output.txt", "w") as output_file:
        output_file.write(content)


convert_to_uppercase("example.txt")