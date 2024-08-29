import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
turtle=Player()

car=CarManager()
screen.listen()
screen.onkey(turtle.up,"Up")
screen.onkey(turtle.down,"Down")
score=Scoreboard()




game_is_on = True
i=0

while game_is_on:

    time.sleep(0.1)
    screen.update()

    car.create_cars()
    for j in car.all_cars:
        if j.distance(turtle)<20:
            score.game_over()
            game_is_on=False
    if turtle.ycor()>240:
        score.increase()
        turtle.refresh()
        car.refresh()

    i+=1
    car.move()
screen.exitonclick()