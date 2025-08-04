from turtle import Turtle
font = ("Courier",25,"normal")
font1 = ("Arial",28,"normal")
class Score(Turtle):
    def __init__(self,x):
        super().__init__()
        self.hideturtle()
        self.score = 0
        self.goto(x,280)
        self.penup()
        self.color("white")
        self.write(f"Score: {self.score}",align="center",font=font)


    def increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score: {self.score}",align="center", font=font)


    def winner(self,player):
        self.goto(0,0)
        self.write(f"The {player} won.",align="center", font= font1)



