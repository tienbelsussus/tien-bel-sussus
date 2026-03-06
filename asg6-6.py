import random

def approximate_pi(points):
    inside_circle = 0

    for i in range(points):
        x = random.uniform(-1, 1)
        y = random.uniform(-1, 1)

        if x**2 + y**2 < 1:
            inside_circle += 1

    pi = 4 * inside_circle / points
    return pi


def main():
    N = int(input("How many random points to generate: "))

    result = approximate_pi(N)

    print("Approximation of pi:", result)


main()