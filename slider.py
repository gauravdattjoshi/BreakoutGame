from turtle import *


class Slider(Turtle):

    def __init__(self):
        super().__init__()
        self.create_slider()

    def move_forward(self):
        self.goto((self.xcor() + 15, self.ycor()))

    def move_backward(self):
        self.goto((self.xcor() - 15, self.ycor()))

    def move_left(self):
        if self.xcor() >= -400:
            self.move_backward()

    def move_right(self):
        if self.xcor() <= 400:
            self.move_forward()

    def create_slider(self):
        self.shape('square')
        self.shapesize(1, 10, 1)
        self.penup()
        self.goto(0, -300)