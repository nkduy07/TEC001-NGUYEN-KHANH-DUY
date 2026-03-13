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

cars = []
for i in range(1, 11):
    reg_num = f"ABC-{i}"
    max_v = random.randint(150, 200)
    cars.append(Car(reg_num, max_v))

race = True
hours_passed = 0

while race:
    hours_passed += 1
    for car in cars:
        speed_change = random.randint(-10, 15)
        car.accelerate(speed_change)
        car.drive(1)

        if car.travelled_distance >= 10000:
            race = False

print(f"The race ended after {hours_passed} hour(s)!")
print("-" * 60)
print(f"{'Registration number':<10} | {'Max speed':<15} | {'Final speed':<15} | {'Distance':<15}")
print("-" * 60)

for car in cars:
    print(
        f"{car.registration_number:<10} | {car.max_speed:>10} km/h | {car.current_speed:>10} km/h | {car.travelled_distance:>10} km")
print("-" * 60)