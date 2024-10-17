from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,x_pos,y_pos):
        super().__init__()
        self.setposition(x_pos, y_pos)
        self.shape("square")
        self.penup()
        self.shapesize(5,1)
        self.color("white")
        self.speed('fastest')

    def move_up(self):
        if self.ycor()==250:
            pass
        else:
            new_y_position=self.ycor()
            new_y_position+=50
            self.goto(self.xcor(),new_y_position)

    def move_down(self):
        if self.ycor() == -250:
            pass
        else:
            new_y_position=self.ycor()
            new_y_position-=50
            self.goto(self.xcor(),new_y_position)