from turtle import Turtle

MOVE_DISTANCE = 10
FINISH_LINE_Y = 420


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.reset()

    def upward(self):
        self.forward(10)

    def reset(self):
        self.shape("turtle")
        self.shapesize(2, 2)
        self.color("black")
        self.penup()
        self.setheading(90)
        self.goto(0, -420)

    def is_at_finish_line(self):
        if self.ycor() >  FINISH_LINE_Y:
            return True
        else:
            return False




