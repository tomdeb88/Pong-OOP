from turtle import Turtle

class Score(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(0, 240)
        self.color('white')
        self.left_p_points = 0
        self.right_p_points=0
        self.display_score()


    def left_scoring(self):
        self.left_p_points+=1
        self.clear()
        self.display_score()

    def right_scoring(self):
        self.right_p_points += 1
        self.clear()
        self.display_score()

    def display_score(self):
        self.write(f"{self.left_p_points} : {self.right_p_points}", align='center', font=("Arial", 30, 'normal'))