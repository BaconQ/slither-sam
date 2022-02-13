from turtle import Turtle
import random

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("triangle")
        self.penup()
        self.shapesize(stretch_wid= 0.9, stretch_len=0.9)
        self.color("yellow")
        self.speed("fastest")
        self.refresh()

        
    #refreshes food
    def refresh(self):
       
        random_x = random.randint(-360,360)
        random_y = random.randint(-360,360)
        self.goto(random_x, random_y)