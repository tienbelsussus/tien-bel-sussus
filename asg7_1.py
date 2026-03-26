class Car:
    def __init__(self, registration_number, maximum_speed):
        self.registration_number = registration_number
        self.maximum_speed = maximum_speed
        self.current_speed = 0
        self.travelled_distance = 0

new_car = Car("ABC-123", 142)
print(new_car.registration_number)
print(new_car.maximum_speed)
print(new_car.current_speed)
print(new_car.travelled_distance)