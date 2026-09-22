from  turtle import Turtle
import random


class FoodMaster(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("blue")
        self.shapesize(0.5,0.5)
        self.shape("circle")
        self.goto(120,70)

    def change_position(self):
        rand_x=random.randint(-245,245)
        rand_y=random.randint(-245,245)
        self.goto(rand_x,rand_y)

