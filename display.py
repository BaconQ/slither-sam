from turtle import Turtle, Screen
class Display(Turtle):
    def __init__(self):
        super().__init__()
        self.screen = Screen()
        self.screen.setup(width=1000, height=1000)
        self.screen.bgcolor("Black")
        self.screen.title("Slither Sam")
        self.screen.tracer(0)
        self.border()
    
    def exit(self):
       self.screen.exitonclick()

    def listen(self):
        self.screen.listen()

    def border(self):
        self.penup()
        self.goto(370,-370)
        self.color("white")
        self.setheading(90)
        self.hideturtle()
        self.pendown()
        for _ in range(4):
            self.fd(740)
            self.left(90)
    
       

