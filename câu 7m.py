import random

while True:
    code_3digit = [random.randint(0, 9) for i in range(3)]
    print("3-digit code (0-9):",str(code_3digit))

    code_4digit = [random.randint(1, 6) for i in range(4)]
    print("4-digit code (1-6):",str(code_4digit))

    choice = input("Generate again? (yes/no): ").lower()

    if choice not in ['yes', 'y']:
        print("Goodbye!")
        break