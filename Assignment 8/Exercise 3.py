class Elevator:
    def __init__(self, bottom, top):
        self.bottom = bottom
        self.top = top
        self.current_floor = bottom
    def floor_up(self):
        if self.current_floor < self.top:
            self.current_floor += 1
            print(f"The elevator is going up. Current floor: {self.current_floor}")
        else:
            print("The elevator is already on the highest floor")
    def floor_down(self):
        if self.current_floor > self.bottom:
            self.current_floor -= 1
            print(f"The elevator is going down. Current floor: {self.current_floor}")
        else:
            print("The elevator is already on the lowest floor")
    def go_to_floor(self, target_floor):
        if self.current_floor < self.bottom or self.current_floor > self.top:
            print("It is not available")
            return
        while self.current_floor > target_floor:
            self.floor_down()
        while self.current_floor < target_floor:
            self.floor_up()
class Building:
    def __init__(self, bottom, top, num_elevators):
        self.bottom = bottom
        self.top = top
        self.elevator = [Elevator(bottom, top) for i in range(num_elevators)]
    def run_elevator(self, elevator_number, destination_floor):
        if 1 <= elevator_number <= len(self.elevator):
            print(f"Elevator {elevator_number} is working")
            selected_elevator = self.elevator[elevator_number]
            selected_elevator.go_to_floor(destination_floor)
        else:
            print("Invalid elevator number")
    def fire_alarm(self):
        for i in self.elevator:
            print(f"The elevator is evacuating")
            i.go_to_floor(1)

if "__main__" == __name__:
    westbay = Building(1,20,5)
    westbay.run_elevator(2,17)
    westbay.run_elevator(1,19)
    westbay.fire_alarm()
