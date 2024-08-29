from turtle import Turtle
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280
MOVE_INCREMENT = 10


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.penup()
        self.goto(STARTING_POSITION)
        self.left(90)
        self.speed=MOVE_DISTANCE
    def up(self):
        if self.ycor()<280:
            y=self.ycor()+self.speed
            self.goto(self.xcor(),y)

    def down(self):
        if self.ycor()>-280:
            y=self.ycor()-MOVE_DISTANCE
            self.goto(self.xcor(),y)
    def refresh(self):
        self.goto(STARTING_POSITION)
        self.speed+=MOVE_INCREMENT


