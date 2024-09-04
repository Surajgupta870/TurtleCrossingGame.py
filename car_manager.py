from turtle import Turtle
from random import choice,randint
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10

class CarManager:
    def __init__(self):
        self.all_cars = []
        self.car_speed = STARTING_MOVE_DISTANCE

    def create_car(self):
         random_chance = randint(1,6)
         if random_chance == 1:
             new_car = Turtle()
             new_car.penup()
             new_car.shape("square")
             new_car.shapesize(1,3)
             new_car.color(choice(COLORS))
             new_car.setheading(180)
             new_car.goto(500,randint(-350,470))
             self.all_cars.append(new_car)

    def move_car(self):
        for car in self.all_cars:
             car.forward(self.car_speed)

    def level_up(self):
        for car in self.all_cars:
            self.car_speed += MOVE_INCREMENT