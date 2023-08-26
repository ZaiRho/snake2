from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')
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
        self.write(f"Score: {self.score}", True, ALIGNMENT, font=FONT)

    def add_score(self):
        self.score +=1
        self.reset()
        self.setup()

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", True, ALIGNMENT, font=('Courier', 20, 'normal'))

