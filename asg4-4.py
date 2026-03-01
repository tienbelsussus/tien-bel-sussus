import re


def redact_phone_numbers(text):
    # Pattern explanation:
    # \b\d{10}\b      → exactly 10 digits (standalone)
    # \+84\d+         → starts with +84 followed by digits
    pattern = r'\b\d{10}\b|\+84\d+'

    return re.sub(pattern, "[REDACTED]", text)


# Example
document = "Call me at 0912345678 or +84987654321. Office number is 1234567890."
print(redact_phone_numbers(document))