from turtle import Screen
class Display:
    def __init__(self):
        screen = Screen()
        screen.setup(width=800, height=800)
        screen.bgcolor("Black")
        screen.title("Slither Sam")
        screen.tracer(0)
        screen.listen()
