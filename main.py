import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Car Cross")
screen.setup(width=1000, height=900)
screen.tracer(0)
screen.listen()
player = Player()
cars = CarManager()
score = Scoreboard()
screen.onkey(player.upward,"Up")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.create_car()
    cars.move_car()
    #Detect when the turtle collide with car
    for car in cars.all_cars:
        if car.distance(player) < 30:
            game_is_on = False
    #Detect when the turtle player has reached the top edge of the screen
    if player.is_at_finish_line():
        score.increase_score()
        player.reset()

screen.exitonclick()