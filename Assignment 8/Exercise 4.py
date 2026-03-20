import random


class Car:
    def __init__(self, registration_number, max_speed):
        self.registration_number = registration_number
        self.max_speed = max_speed
        self.current_speed = 0
        self.travelled_distance = 0

    def accelerate(self, change):
        new_speed = self.current_speed + change
        if new_speed > self.max_speed:
            self.current_speed = self.max_speed
        elif new_speed < 0:
            self.current_speed = 0
        else:
            self.current_speed = new_speed

    def drive(self, hours):
        self.travelled_distance += self.current_speed * hours


class Race:
    def __init__(self, name, distance, cars):
        self.name = name
        self.distance = distance
        self.cars = cars

    def hour_passes(self):
        for car in self.cars:
            car.accelerate(random.randint(-10, 15))
            car.drive(1)

    def print_status(self):
        print(f"\n--- {self.name} ---")
        print(f"{'Registration':<15} | {'Max speed':<10} | {'Current speed':<15} | {'Distance':<10}")
        print("-" * 70)
        for car in self.cars:
            print(
                f"{car.registration_number:<15} | {car.max_speed:<10} | {car.current_speed:<15} | {car.travelled_distance:<10}")

    def race_finished(self):
        for car in self.cars:
            if car.travelled_distance >= self.distance:
                return True
        return False


if __name__ == "__main__":
    car_list = []
    for i in range(1, 11):
        m_speed = random.randint(100, 200)
        car_list.append(Car(f"ABC-{i}", m_speed))

    big_race = Race('Grand Demolition Derby', 8000, car_list)
    hours_passed = 0

    while not big_race.race_finished():
        big_race.hour_passes()
        hours_passed += 1

        if hours_passed % 10 == 0:
            print(f"\n--- After {hours_passed} hours ---")
            big_race.print_status()

    print(f"\nThe race ended after {hours_passed} hours!")
    big_race.print_status()