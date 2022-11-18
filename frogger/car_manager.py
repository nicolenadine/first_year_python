from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_SPEED_INCREMENT = 5


class CarManager:

    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    # random is used to keep a car from being generated every time
    # the screen updates. Instead there is a chance a new car will be
    # generated when screen refreshes but not every time.
    def create_car(self):
        random_chance = random.randint(1,6)
        if random_chance == 1:
            new_car = Turtle("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_yposition = random.randint(-250, 250)
            new_car.goto(300, random_yposition)
            self.all_cars.append(new_car)

    def move_cars(self):
        for car in self.all_cars:
            car.backward(self.car_speed)


    def level_up(self):
        self.car_speed += MOVE_SPEED_INCREMENT
