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
            segment = Turtle(shape="square")
            segment.color("white")
            segment.penup()
            segment.goto(position)
            self.body.append(segment)

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
    
    
    def turn(self):
        self.screen.onkey(self.left, "a")
        self.screen.onkey(self.right, "d")
        self.screen.onkey(self.up, "w")
        self.screen.onkey(self.down, "s")