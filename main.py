from turtle import Screen
from paddle import Paddle
from ball import Ball
import time

screen = Screen()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)


right_paddle=Paddle(350,0)
left_paddle=Paddle(-350,0)
ball=Ball()


screen.onkey(right_paddle.move_up,'Up')
screen.onkey(right_paddle.move_down,'Down')
screen.onkey(left_paddle.move_up,'w')
screen.onkey(left_paddle.move_down,'s')

game_on=True
while game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    #hitting up and down wall
    if ball.ycor()==280 or ball.ycor()==-280:
        ball.bounce()

    #contact if paddle
    if ball.xcor()>320 and ball.distance(right_paddle)<50 or ball.xcor()<-320 and ball.distance(left_paddle)<50:
        ball.hitting_paddle()
    if ball.xcor() < -340 or ball.xcor() > 340:
        print('score')

