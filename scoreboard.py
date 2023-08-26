from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.setup()


    def setup(self):
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", True, "center", font=('Arial', 12, 'normal'))

    def add_score(self):
        self.score +=1
        self.reset()
        self.setup()
