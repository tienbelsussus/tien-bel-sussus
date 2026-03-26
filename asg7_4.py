import random

class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, speed_change):
        self.current_speed += speed_change
        if self.current_speed > self.maximum_speed:
            self.current_speed = self.maximum_speed
        elif self.current_speed < 0:
            self.current_speed = 0

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours

cars = []
for i in range(1, 11):
    max_speed = random.randint(150, 200)
    cars.append(Car(f"ABC-{i}", max_speed))

race_over = False
while not race_over:
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)
        if car.travelled_distance >= 10000:
            race_over = True

print(f"{'Reg Num':<10} | {'Max Speed':<10} | {'Cur Speed':<10} | {'Distance':<10}")
print("-" * 47)
for car in cars:
    print(f"{car.registration_number:<10} | {car.maximum_speed:<10} | {car.current_speed:<10} | {car.travelled_distance:<10}")