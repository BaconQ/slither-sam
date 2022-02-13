from turtle import Turtle
ALIGNMENT = "center"
FONT =  ("courier", 24, "bold")

file = open("data.txt", mode="r")
HIGH_SCORE = file.read()
file.close()


class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.highscore = HIGH_SCORE
        self.color("white")
        self.penup()
        self.goto(0,400)
        self.hideturtle()
        self.score_board()
        
        
        
    def score_board(self):
        self.write(f"Score: {self.score} HighScore: {self.highscore} ", align = ALIGNMENT, font= FONT)
        
    def reset(self):
        self.clear()
        if self.score > int(self.highscore):
            self.highscore = self.score
            file = open("data.txt", mode="w")
            file.write(f"{self.highscore}")
            file.close()
            
        self.score = 0
        self.score_board()
        

    def update(self):
        self.score += 1
        self.clear()
        self.score_board()

