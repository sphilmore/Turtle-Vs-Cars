from turtle import Turtle
FONT = ("Courier", 24, "normal")
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level_up = 0
        self.game_over = "GameOver"
        self.level_update()
    def level_update(self):
        self.clear()
        self.goto(-280, 260)
        self.write(f"level:{self.level_up}", align= 'left', font=FONT)
    def score_update(self):
        self.level_up += 1
        self.level_update()
    def over(self):
        self.goto(0, 0)
        self.write(self.game_over, align="center", font= FONT)




