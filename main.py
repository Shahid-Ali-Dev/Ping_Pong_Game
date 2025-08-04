from turtle import Screen
from structure import Ping
from Ball import Ball
import time
from scoreboard import Score

b = Ball()
p = Ping()
s = Screen()
s.tracer(0)
score1 = Score(-180)
score2 = Score(180)

s.bgcolor("black")
s.title("Ping Pong Game")

p.players()
s.listen()
s.update()
time.sleep(1)
game_is_on = True

while game_is_on:

    time.sleep(b.move_speed)
    s.update()
    s.onkeypress(p.l, "Left")
    b.go_r()
    if b.ycor() >= 320 or b.ycor() <= -320:
        b.direction()

    elif b.distance(p.lst[0]) < 50 and b.xcor() > 340 or b.distance(p.lst[1]) < 50 and b.xcor() < -340:
        b.reverse()

    elif b.xcor() > 380:
        b.reset()
        s.update()
        score1.increase()
        time.sleep(1.5)

    elif b.xcor() < -380:
        b.reset()
        s.update()
        score2.increase()
        time.sleep(1.5)

    s.onkeypress(p.r, "Right")
    if score1.score > score2.score and score1.score == 10:
        score1.winner("Left Player")
        game_is_on = False

    elif score2.score > score1.score and score2.score == 10:
        score2.winner("Right Player")
        game_is_on = False


s.exitonclick()