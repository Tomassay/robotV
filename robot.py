from turtle import Turtle

tavolsag = 0

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180
WALL_POSX = 935
WALL_NEGX = -945
WALL_POSY = 520
WALL_NEGY = -460


class Robot(Turtle):

    def __init(self):
        pass

    def position(self):
        return self.robot_part.pos()

    def move(self):

        # print('YCOR',self.ycor())
        # print('XCOR', self.xcor())
        self.forward(MOVE_DISTANCE)

    def move_up(self):
        if self.heading() == LEFT or self.heading() == RIGHT:
            self.setheading(UP)

    def move_down(self):
        if self.heading() == LEFT or self.heading() == RIGHT:
            self.setheading(DOWN)

    def move_right(self):
        if self.heading() == UP or self.heading() == DOWN:
            self.setheading(RIGHT)

    def move_left(self):
        if self.heading() == UP or self.heading() == DOWN:
            self.setheading(LEFT)

    def on_dirt(self, dirt):
        return self.pos() == dirt.pos()

    def detect_obstacle(self):
        return self.xcor() > WALL_POSX or self.xcor() < WALL_NEGX\
               or self.ycor() > WALL_POSY or self.ycor() < WALL_NEGY

    def turn_on_edges(self):
        print('heading',self.heading())
        if self.heading() == 270:
            self.setheading(0)
            #self.forward(10)
        else:
            self.setheading(self.heading() + 90)
        self.forward(20)

    def move_spiral(self):
        global tavolsag
        print('előtte heading',self.heading())
        #self.setheading(self.heading()+11)
        self.right(15)
        print('utána heading',self.heading())
        self.forward(tavolsag)
        tavolsag += 0.1
        print('tavolsag', tavolsag)



