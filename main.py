from snake import Snake
from display import Display
from food import Food

display = Display()
sam = Snake()
food = Food()
sam.turn()

is_snake_alive = True
while is_snake_alive:
    sam.move()
    
    if sam.head.distance(food) < 15:
        food.refresh()




