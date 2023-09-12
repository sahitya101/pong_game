from turtle import Turtle,Screen
from paddle import paddle
from boll import Boll
from scoreboard import Scoreboard
import time
screen = Screen()
screen.bgcolor('black')
screen.setup(width=800,height=600)
screen.title('pong')
screen.tracer(0)

r_paddle = paddle((350,0))
l_paddle = paddle((-350,0))
boll = Boll((0, 0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.go_up,"Up")
screen.onkey(r_paddle.go_down,"Down")
screen.onkey(l_paddle.go_up,"w")
screen.onkey(l_paddle.go_down,"s")
game_is_on = True
while game_is_on:
    time.sleep(boll.move_speed)
    screen.update()
    boll.move()
    if boll.ycor() > 280 or boll.ycor() < -280:
        boll.bounce_y()
    if boll.distance(r_paddle) < 50 and boll.xcor() > 320 or boll.distance(l_paddle) < 50 and boll.xcor() < -320:
        boll.bounce_x()
    if boll.xcor() > 380:
            boll.reset_position()
            scoreboard.l_point()
    if  boll.xcor() < -380:
        boll.reset_position()
        scoreboard.r_point()

screen.exitonclick()