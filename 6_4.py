from random import choice


class Car:
    """ Main car """
    direction = ["north", "northeast", "east", "southeast",
                 "south", "southwest", "west", "northwest"]

    def __init__(self, n, c, s, p=False):
        self.name = n
        self.color = c
        self.speed = s
        self.is_police = p
        print(f'New car: {n} has a color: {c}.\nIs this a police car? {p}')

    def go(self):
        print(f'{self.name}: Drive')

    def stop(self):
        print(f'{self.name}: Stopped')

    def turn(self):
        print(f'{self.name}: Turning {choice(self.direction)}.')

    def show_speed(self):
        return f'{self.name}: Speed: {self.speed}.'


class TownCar(Car):
    """ City Car """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Spee-up' if self.speed > 60 else super().show_speed()


class WorkCar(Car):
    """ Cargo truck """

    def show_speed(self):
        return f'{self.name}: Car speed: {self.speed}. Spee-up' if self.speed > 40 else super().show_speed()


class SportCar(Car):
    """ Sports Car """


class PoliceCar(Car):
    """ Patrol car """

    def __init__(self, n, c, s):
        super().__init__(n, c, s, p=True)


police_car = PoliceCar('"Police vehicle"', 'white', 80)
work_car = WorkCar('"Lorry"', 'green', 40)
sport_car = SportCar('"Sports car"', 'red', 120)
town_car = TownCar('"Minicar"', 'yellow', 65)

list_of_cars = [police_car, work_car, sport_car, town_car]

for i in list_of_cars:
    i.go()
    print(i.show_speed())
    i.turn()
    i.stop()
    print()
