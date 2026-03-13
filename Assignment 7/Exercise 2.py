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

my_car = Car("ABC-123", 142)
print(f"Registration number: {my_car.registration_number}")
print(f"Max speed: {my_car.max_speed} km/h")
print(f"Current speed: {my_car.current_speed} km/h")
print(f"Travelled distance: {my_car.travelled_distance} km")

my_car.accelerate(30)
my_car.accelerate(70)
my_car.accelerate(50)
print(f"Speed after acceleration: {my_car.current_speed} km/h")

my_car.accelerate(-200)
print(f"Speed after brake: {my_car.current_speed} km/h")