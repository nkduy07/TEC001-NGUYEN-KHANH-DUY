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


if "__main__" == __name__:
    a = Elevator(1, 10)
    a.go_to_floor(6)
    a.go_to_floor(1)
