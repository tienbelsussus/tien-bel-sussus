def is_valid_hex_color(color):
    # Check total length
    if len(color) != 7:
        return False

    # Check it starts with #
    if color[0] != "#":
        return False

    # Allowed hexadecimal characters
    allowed = "0123456789ABCDEFabcdef"

    # Check each character after #
    for char in color[1:]:
        if char not in allowed:
            return False

    return True


# Example tests
print(is_valid_hex_color("#A1B2C3"))  # True
print(is_valid_hex_color("#ffffff"))  # True
print(is_valid_hex_color("#123abc"))  # True
print(is_valid_hex_color("123abc"))  # False
print(is_valid_hex_color("#12G45Z"))  # False
print(is_valid_hex_color("#1234"))  # False