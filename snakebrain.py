from snake import Snake
from display import Display
from food import Food
from score import Score

class SnakeBrain:
    def __init__(self):
        self.display = Display()
        self.sam = Snake()
        self.food = Food()
        self.score = Score()
        self.sam.turn()
        self.display.listen()

        

    def start_game(self):
        is_snake_alive = True
        while is_snake_alive:

            self.sam.move()

            if self.sam.head.distance(self.food) < 15:
                self.food.refresh()
                self.score.update()
                self.sam.extend()

            if self.sam.head.xcor() > 370 or self.sam.head.xcor() < -370 or self.sam.head.ycor() > 370 or self.sam.head.ycor() < -370:
                self.score.reset()
                self.sam.reset()
                

            for segments in self.sam.body[1:]:
                if self.sam.head.distance(segments) < 10:
                    self.score.reset()
                    self.sam.reset()
                    
