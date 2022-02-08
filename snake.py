from turtle import Turtle, Screen
import time

STARTING_POSITION = [(0,0), (-20,0), (-40,0)]
UP = 90
DOWN = 270
RIGHT = 0
LEFT = 180

class Snake:
 
    def __init__(self):
        self.body = []
        self.screen = Screen()
        self.speed = 20
        self.create_snake()
        self.head = self.body[0]
        
#creates snake
    def create_snake(self):
        for position in STARTING_POSITION:
            self.add_body(position)
            

    def add_body(self, position):
        segment = Turtle(shape="square")
        segment.color("white")
        segment.penup()
        segment.goto(position)
        self.body.append(segment)

    def extend(self):
        self.add_body(self.body[-1].position())

#moves snake 
    def move(self):
        self.screen.update()
        time.sleep(0.1)
        for i in range(len(self.body) -1, 0, -1):
            new_x = self.body[i-1].xcor()
            new_y = self.body[i-1].ycor()
            self.body[i].goto(new_x, new_y)
        self.head.fd(self.speed)
                
#turns snake
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)


    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    
    #listen to keystrokes
    def turn(self):
        time.sleep(0.01)
        self.screen.onkeypress(self.left, "a")
        self.screen.onkeypress(self.right, "d")
        self.screen.onkeypress(self.up, "w")
        self.screen.onkeypress(self.down, "s")