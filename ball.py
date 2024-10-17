from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color('white')
        self.penup()
        self.x_value=10
        self.y_value=10

    def move(self):
        x_pos=self.xcor()+self.x_value
        y_pos=self.ycor()+self.y_value
        self.goto(x_pos,y_pos)

    def bounce(self):
        self.y_value*=-1

    def hitting_paddle(self):
        self.x_value*=-1

    def missed(self):
        self.goto(0,0)
        self.x_value *= -1