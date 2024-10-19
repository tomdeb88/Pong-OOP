from turtle import Screen
from paddle import Paddle
from ball import Ball
import time
from score import Score

screen = Screen()
screen.setup(width=800 , height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)


right_paddle=Paddle(350,0)
left_paddle=Paddle(-350,0)
ball=Ball()
score=Score()



screen.onkey(right_paddle.move_up,'Up')
screen.onkey(right_paddle.move_down,'Down')
screen.onkey(left_paddle.move_up,'w')
screen.onkey(left_paddle.move_down,'s')

game_on=True

while game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()

    #hitting up and down wall
    if ball.ycor()==270 or ball.ycor()==-270:
        ball.bounce()

    #contact with paddle
    if ball.xcor()>320 and ball.distance(right_paddle)<50 or ball.xcor()<-320 and ball.distance(left_paddle)<50:
        ball.hitting_paddle()


    #missed ball by left paddle
    if ball.xcor() < -380:
        ball.missed()
        score.right_scoring()

    #missed ball by right paddle
    if ball.xcor() > 380:
        ball.missed()
        score.left_scoring()

    print(ball.ball_speed)





