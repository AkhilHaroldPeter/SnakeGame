from turtle import Turtle

ALIGNMENT = 'center'
FONT = ("Comic Sans MS",24,'normal')

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.final_score = 0
        self.color("white")
        self.penup()
        self.goto(0, 300)
        self.update_scoreboard()
        self.hideturtle()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def Increase_Score(self):
        self.score += 1
        self.final_score += 1
        self.update_scoreboard()

    def game_over(self):
        self.goto(0, 0)
        self.final_score = self.score
        self.write('GAME OVER',align=ALIGNMENT, font=FONT)

    def reset_scoreboard(self):
        self.score = 0
        self.update_scoreboard()