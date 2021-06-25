STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
MOVE_DOWN = 10
FINISH_LINE_Y = 280
from turtle import Turtle, Screen
class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.color("black")
        self.penup()
        self.goto(STARTING_POSITION)
        self.setheading(90)
    def starting_point(self):
        self.goto(STARTING_POSITION)
    def move(self):
        self.forward(MOVE_DISTANCE)
    def move_down(self):
        self.backward(MOVE_DOWN)
    def move_right(self):
        new_x = self.xcor() + 10
        self.goto(new_x, self.ycor())
    def move_left(self):
        new_m = self.xcor() - 10
        self.goto(new_m, self.ycor())
    def reset_turtle(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False




