from turtle import Turtle
ALIGNMENT = "center"
FONT =  ("courier", 24, "bold")

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0,360)
        self.hideturtle()
        self.score_board()
        
        
        
    def score_board(self):
        self.write(f"Score: {self.score} ", align = ALIGNMENT, font= FONT)
        
    def game_over(self):
        self.goto(0,0)
        self.write(f"GAME OVER!", align = ALIGNMENT, font= FONT)
        

    def update(self):
        self.score += 1
        self.clear()
        self.score_board()

