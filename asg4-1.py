def is_valid_course_code(code):
    # Check length
    if len(code) != 6:
        return False

    # Check first 3 characters are uppercase letters
    if not code[:3].isupper() or not code[:3].isalpha():
        return False

    # Check last 3 characters are digits
    if not code[3:].isdigit():
        return False

    return True


# Example tests
print(is_valid_course_code("TEC001"))  # True
print(is_valid_course_code("tec001"))  # False
print(is_valid_course_code("TE1001"))  # False
print(is_valid_course_code("ABC12"))  # False