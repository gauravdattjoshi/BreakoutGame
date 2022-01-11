import random
from turtle import *


class BubbleBox():
    def __init__(self):
        self.width_sum = 0
        self.turtles_list = []
        self.create_box_layers()

    def create_bubbles_row(self, height):
        loop_count = 0
        continue_loop = True

        while continue_loop:
            # NO CHANGE REQUIRED
            t = Turtle(shape='square')
            t.penup()
            t.hideturtle()
            t.speed(0)
            t.fillcolor((random.randint(0, 255), random.randint(10, 255), random.randint(0, 255)))

            # Creating Width of turtle
            widths = 10
            self.width_sum += widths
            # create turtle
            t.shapesize(2, 4, 4)
            position = 400 - loop_count * 90
            t.goto(position, height)
            loop_count += 1
            t.showturtle()
            self.turtles_list.append(t)
            if position <= -380:
                continue_loop=False

    def create_box_layers(self):
        for i in range(5):
            height = 350
            self.create_bubbles_row(height=(height - i * 50))
