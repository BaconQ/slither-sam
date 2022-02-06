from snake import Snake
from turtle import Screen

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("Black")
screen.title("Slither Sam")
screen.tracer(0)
screen.listen()
sam = Snake()

is_snake_alive = True

while is_snake_alive:
    sam.move()
    screen.onkey(sam.left, "a")
    screen.onkey(sam.right, "d")
    screen.onkey(sam.up, "w")
    screen.onkey(sam.down, "s")
    

screen.exitonclick()



