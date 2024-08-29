from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:
    def __init__(self):
        self.all_cars = []
        self.speed = STARTING_MOVE_DISTANCE
        self.car_creation_chance = 6  # Higher means fewer cars initially

    def create_cars(self):
        random_n = random.randint(1, self.car_creation_chance)
        if random_n == 1:
            new_car = Turtle()
            new_car.shape("square")
            new_car.shapesize(stretch_wid=1, stretch_len=2)
            new_car.penup()
            new_car.color(random.choice(COLORS))
            random_y = random.randint(-240, 230)
            new_car.goto(300, random_y)
            self.all_cars.append(new_car)

    def move(self):
        for car in self.all_cars:
            car.backward(self.speed)

    def refresh(self):
        self.speed += MOVE_INCREMENT
        # Increase the likelihood of car creation by lowering the threshold
        if self.car_creation_chance > 1:
            self.car_creation_chance -= 1
