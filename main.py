import random
from turtle import Screen, Turtle
from robot import Robot
from dirt import Dirt
import time
from map import make_map
from pandas import *


screen = Screen()
screen.screensize(canvwidth=800, canvheight=600)
screen.bgcolor("white")
screen.title("Robot Vacuum Simulation")
screen.tracer(0)
screen.setup(width=1.0,height=1.0,startx=None,starty=None)

RIGHT_UP = (935, 520)
LEFT_DOWN = (-945, -460)
RIGHT_DOWN = (935, -460)
LEFT_UP = (-945, 520)

print(screen.canvheight)

simulation_on: bool = True
robi = Robot("turtle")
robi.color("red")
dirtbag = []
bag_size = random.randint(1,1000)

for _ in range(0, bag_size):
    x = Dirt()
    dirtbag.append(x)
    x.place_dirt()

#map = make_map(10,10,4)
#print(DataFrame(map))


def draw_edges():

    line = Turtle()
    line.pu()
    line.goto(RIGHT_UP)
    line.pd()
    line.goto(RIGHT_DOWN)
    line.goto(LEFT_DOWN)
    line.goto(LEFT_UP)
    line.goto(RIGHT_UP)
    line.hideturtle()


draw_edges()

def map_matrix():
    pass

map_matrix()

while simulation_on:
    screen.update()
    time.sleep(0.1)
    for dirt in dirtbag:
        if robi.distance(dirt) < 25:
            dirt.clean_dirt()
    if not robi.detect_obstacle():
        robi.move_spiral()
    else:
        print("PLACCS")



    #robi.move()


    #robi.turn_on_edges()
    #robi.move()


    # if robi.detect_obstacle():
    #     print('kopp')
    #     robi.down()
    #     robi.move()


screen.exitonclick()