import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
player = Player()
car = CarManager()
score = Scoreboard()
screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()
screen.onkey(player.move, "Up")
screen.onkey(player.move_down, "Down")
screen.onkey(player.move_right, "Right")
screen.onkey(player.move_left, "Left")
game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.move_cars()
    player.reset_turtle()
    score.level_update()
    #Detect collision with car
    for cars in car.all_car:
        if cars.distance(player) < 20:
            game_is_on = False
            score.over()
    if player.reset_turtle():
        player.starting_point()
        car.level_up()
        score.score_update()







screen.exitonclick()