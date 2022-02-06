from snake import Snake
from turtle import Screen
from food import Food

screen = Screen()
screen.setup(width=800, height=800)
screen.bgcolor("Black")
screen.title("Slither Sam")
screen.tracer(0)
screen.listen()
sam = Snake()
food = Food()
screen.onkey(sam.left, "a")
screen.onkey(sam.right, "d")
screen.onkey(sam.up, "w")
screen.onkey(sam.down, "s")


is_snake_alive = True

while is_snake_alive:
    sam.move()
    
    if sam.head.distance(food) < 15:
        food.refresh()
    

screen.exitonclick()



