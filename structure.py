from turtle import Turtle,Screen
s = Screen()
controlled_sides = None
class Ping(Turtle):

    def __init__(self):
        super().__init__()
        self.lst = []
        self.hideturtle()

    def up(self):
        if controlled_sides == "right" and self.lst[0].ycor() < 270:
            new_y = self.lst[0].ycor() + 15
            self.lst[0].goto(360, new_y)

        elif controlled_sides == "left" and self.lst[1].ycor() < 270 :
            new_y = self.lst[1].ycor() + 15
            self.lst[1].goto(-368, new_y)

    def down(self):
        if controlled_sides == "left" and self.lst[1].ycor() > -260:
            new_y = self.lst[1].ycor() - 15
            self.lst[1].goto(-368, new_y)

        elif controlled_sides == "right" and self.lst[0].ycor() > -260:
            new_y = self.lst[0].ycor() - 15
            self.lst[0].goto(360, new_y)

    def bind_controls(self):
        s.onkeypress(self.up, "Up")
        s.onkeypress(self.down, "Down")

    def l(self):
        global controlled_sides
        controlled_sides = "left"
        self.bind_controls()


    def r(self):
        global controlled_sides
        controlled_sides = "right"
        self.bind_controls()



    def players(self):
        y = 20
        x = 360
        for i in range(2):
            if i == 1:
                x = -368
                y = 20
            t = Turtle(shape="square")
            t.penup()
            t.color("blue")
            t.goto(x,y)
            t.shapesize(5,1)
            y -= 20
            self.lst.append(t)

        y = 300
        for i in range(21):
            z = Turtle(shape= "square")
            z.penup()
            z.color("white")
            z.shapesize(1,0.04)
            z.goto(0,y)
            y -= 30
