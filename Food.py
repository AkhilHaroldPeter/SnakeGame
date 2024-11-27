from turtle import Turtle
import random

FOOD_SHAPE = 'circle'
FOOD_COLOR = 'blue'

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape(FOOD_SHAPE)
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(FOOD_COLOR)
        self.speed('fastest')
        self.refresh_food()

    def refresh_food(self):
        self.goto(random.randint(-320, 320), random.randint(-320, 320))
