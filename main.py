from snake import Snake
from display import Display
from food import Food
from score import Score

display = Display()
sam = Snake()
food = Food()
score = Score()

sam.turn()
display.listen()

is_snake_alive = True
while is_snake_alive:
    sam.move()
    
    if sam.head.distance(food) < 15:
        food.refresh()
        score.update()
        sam.extend()

    if sam.head.xcor() > 380 or sam.head.xcor() < -400 or sam.head.ycor() > 390 or sam.head.ycor() < -390:
        is_snake_alive = False
        score.game_over()

    for segments in sam.body[1:]:
        if sam.head.distance(segments) < 10:
            is_snake_alive = False
            score.game_over()
            
display.exit()
