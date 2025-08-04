from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("circle")
        self.color("yellow")
        self.shapesize(0.8)
        self.x = 10
        self.y = 10
        self.move_speed = 0.03

    def go_r(self):
        self.speed("slowest")
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x,new_y)

    def direction(self):
        self.y *= -1

    def reverse(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.goto(0, 0)
        self.move_speed = 0.03
        self.reverse()






