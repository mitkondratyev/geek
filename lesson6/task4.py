class Car():
    directions = ("left", "right")

    def __init__(self, name, color, speed = 0, is_police = False):
        self.name = name
        self.color = color
        self.speed = float(speed)
        self.is_police = bool(is_police)

    def go(self):
        print("Car is driving")

    def stop(self):
        print("Car is stopped")

    def turn(self, direction):
        if direction in self.directions:
            print(f'Car turned to {direction}')

    def show_speed(self):
        print(self.speed)

class TownCar(Car):

    def __init__(self, name, color, speed = 0):
        super().__init__(name, color, speed)

    def show_speed(self):
        if self.speed > 60:
            print(f'Over speed')

class SportCar(Car):

    def __init__(self, name, color, speed = 0):
        super().__init__(name, color, speed)

class WorkCar(Car):

    def __init__(self, name, color, speed = 0):
        super().__init__(name, color, speed)

    def show_speed(self):
        if self.speed > 40:
            print(f'Over speed')

class PoliceCar(Car):

    def __init__(self, name, color, speed = 0):
        super().__init__(name, color, speed, True)

if __name__ == '__main__':
    print("\nTown Car")
    town = TownCar("Toyota Camry", "White", 60)
    town.go()
    town.turn("left")
    town.turn("right")
    town.stop()
    town.show_speed()
    print("\nTown Car speed > 60")
    town = TownCar("Toyota Camry", "Black", 70)
    town.go()
    town.turn("left")
    town.turn("right")
    town.stop()
    town.show_speed()
    print("\nSport Car")
    sport = SportCar("Porsche", "Black", 370)
    sport.go()
    sport.turn("left")
    sport.turn("right")
    sport.stop()
    sport.show_speed()
    print("\nWork Car")
    work = WorkCar("UAZ", "White", 40)
    work.go()
    work.turn("left")
    work.turn("right")
    work.stop()
    work.show_speed()
    print("\nWork Car speed > 40")
    work = WorkCar("UAZ", "Black", 90)
    work.go()
    work.turn("left")
    work.turn("right")
    work.stop()
    work.show_speed()
    print("\nPolice Car")
    police = PoliceCar("Lada", "Blue", 90)
    police.go()
    police.turn("left")
    police.turn("right")
    police.stop()
    police.show_speed()