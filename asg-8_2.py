import random

# ======================
# ELEVATOR CLASS
# ======================

class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current = bottom   # luôn bắt đầu ở tầng thấp nhất

    def floor_up(self):
        if self.current < self.top:
            self.current += 1
            print(f"Elevator now at floor {self.current}")

    def floor_down(self):
        if self.current > self.bottom:
            self.current -= 1
            print(f"Elevator now at floor {self.current}")

    def go_to_floor(self, target):
        while self.current < target:
            self.floor_up()
        while self.current > target:
            self.floor_down()


# ======================
# BUILDING CLASS
# ======================

class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevators = []

        # tạo danh sách thang máy
        for i in range(num_elevators):
            self.elevators.append(Elevator(bottom, top))

    def run_elevator(self, number, destination):
        print(f"\nRunning elevator {number} to floor {destination}")
        self.elevators[number].go_to_floor(destination)

    def fire_alarm(self):
        print("\nFIRE ALARM! All elevators go to bottom floor.")
        for i, elevator in enumerate(self.elevators):
            print(f"Elevator {i}:")
            elevator.go_to_floor(self.bottom)


# ======================
# CAR CLASS
# ======================

class Car:
    def __init__(self, reg, max_speed):
        self.reg = reg
        self.max_speed = max_speed
        self.speed = 0
        self.distance = 0

    def accelerate(self, change):
        self.speed += change

        if self.speed < 0:
            self.speed = 0
        if self.speed > self.max_speed:
            self.speed = self.max_speed

    def drive(self, hours):
        self.distance += self.speed * hours


# ======================
# RACE CLASS
# ======================

class Race:
    def __init__(self, name, km, cars):
        self.name = name
        self.km = km
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            change = random.randint(-10, 15)
            car.accelerate(change)
            car.drive(1)

    def print_status(self):
        print("\n--- STATUS ---")
        print(f"{'Car':<10}{'Speed':<10}{'Distance':<10}")
        for car in self.cars:
            print(f"{car.reg:<10}{car.speed:<10}{car.distance:<10}")

    def race_finished(self):
        for car in self.cars:
            if car.distance >= self.km:
                return True
        return False


# ======================
# MAIN PROGRAM
# ======================

if __name__ == "__main__":

    # ----- Elevator test -----
    print("=== Elevator Test ===")
    h = Elevator(1, 10)

    h.go_to_floor(5)   # đi lên tầng 5
    h.go_to_floor(1)   # quay về tầng 1


    # ----- Building test -----
    print("\n=== Building Test ===")
    building = Building(1, 10, 3)

    building.run_elevator(0, 6)
    building.run_elevator(1, 8)

    building.fire_alarm()


    # ----- Race simulation -----
    print("\n=== Race Simulation ===")

    cars = []
    for i in range(10):
        cars.append(Car(f"ABC-{i+1}", random.randint(100, 200)))

    race = Race("Grand Demolition Derby", 8000, cars)

    hours = 0
    while not race.race_finished():
        hours += 1
        race.hour_passes()

        if hours % 10 == 0:
            print(f"\nAfter {hours} hours:")
            race.print_status()

    print(f"\nRace finished in {hours} hours!")
    race.print_status()