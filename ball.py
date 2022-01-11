import turtle
from turtle import *


class Ball(Turtle):
    """Ball class deals everything related to ball movement"""

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.create_ball()
        self.showturtle()
        self.x_cor = 3
        self.y_cor = 3
        self.move_speed =0.1

    def move_up_down(self):
        self.y_cor *= -1

    def move_left_right(self):
        self.x_cor *= -1

    def create_ball(self):
        self.shape('circle')
        self.penup()
        self.goto((0, 0))

    def move_ball(self):

        self.goto((self.xcor() + self.x_cor, self.ycor() + self.y_cor))

