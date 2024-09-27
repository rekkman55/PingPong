from turtle import Screen, Turtle
from paddle import Paddle
from the_ball import Ball
from scoreboard import Scoreboard
import time

screen = Screen()
screen.bgcolor("red")
screen.setup(width=800,height=600)
screen.title("Kung Fu")
screen.tracer(0)

r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball()
scoreboard = Scoreboard()
# top_paddle = Paddle((100, 100))



screen.listen()
screen.onkey(r_paddle.go_up, "Up")
screen.onkey(r_paddle.go_down, "Down")

screen.onkey(l_paddle.go_up, "w")
screen.onkey(l_paddle.go_down, "s")

game_is_on = True
while game_is_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    #detect ball
    if ball.ycor() > 300 or ball.ycor() < -300:
        ball.bounce_y()

    #detect collision with paddle
    if ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.bounce_x()

    #detect rpaddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_point()

    #detect lpaddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()


screen.exitonclick()
