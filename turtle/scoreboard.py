from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
        def __init__(self):
            super().__init__()
            self.score = 0
            self.color("black")
            self.penup()
            self.goto(0, 260)
            self.speed("fastest")
            self.hideturtle()

            self.write(f"level:{self.score}", align="center", font=FONT)
        def increase(self):
            self.score+=1
            self.clear()
            self.write(f"Score:{self.score}", align="center", font=FONT)
        def game_over(self):
            self.goto(0, 0)
            self.color("green")
            self.write(f"GAME OVER", align="center", font=("Arial", 40, "normal"))


