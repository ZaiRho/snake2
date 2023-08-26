from turtle import Turtle

ALIGNMENT = "center"
FONT = ('Courier', 14, 'normal')


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.set_high_score()
        self.setup()

    def set_high_score(self):
        with open("data.txt", mode="r") as file:
            content = file.read()
        self.high_score = int(content)

    def setup(self):
        self.penup()
        self.color("white")
        self.ht()
        self.goto(0, 280)
        self.write(f"High Score: {self.high_score} Current Score: {self.score}", True, ALIGNMENT, font=FONT)

    def add_score(self):
        self.score += 1
        self.reset()
        self.setup()

    def game_over(self):
        self.overwrite_high_score()
        self.goto(0, 0)
        self.write("GAME OVER!", True, ALIGNMENT, font=('Courier', 20, 'normal'))

    def overwrite_high_score(self):
        if self.score > self.high_score:
            with open("data.txt", mode="w") as file:
                file.write(str(self.score))


