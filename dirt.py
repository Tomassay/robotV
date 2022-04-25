from turtle import Turtle
import random_coord

class Dirt(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("classic")
        self.pu()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("black")
        self.speed("fastest")

    def place_dirt(self):

        coordinates = random_coord.get_random_coord()
        self.goto(coordinates)
        #print(coordinates)

    def clean_dirt(self):
        self.goto(2000,2000)