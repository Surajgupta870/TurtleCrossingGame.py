from turtle import Turtle
FONT = ("Courier", 24, "normal")

class Scoreboard(Turtle):
   def __init__(self):
       super().__init__()
       self.score = 0
       self.keep_score()

   def keep_score(self):
       self.penup()
       self.hideturtle()
       self.goto(-480, 400)
       self.color("black")
       self.write(f"level: {self.score}", font=FONT)

   def increase_score(self):
       self.clear()
       self.score += 1
       self.keep_score()










