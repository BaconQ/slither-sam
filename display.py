from turtle import Screen
class Display():
    def __init__(self):
        self.screen = Screen()
        self.screen.setup(width=800, height=800)
        self.screen.bgcolor("Black")
        self.screen.title("Slither Sam")
        self.screen.tracer(0)
    
    def exit(self):
       self.screen.exitonclick()

    def listen(self):
        self.screen.listen()

    
       

