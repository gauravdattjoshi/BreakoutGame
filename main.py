import turtle
from turtle import *

from ball import Ball
from bubbleBox import BubbleBox
from slider import Slider

screen = Screen()
screen.setup(width=900, height=800)
screen.listen()
screen.colormode(cmode=255)
slider = Slider()


score = Turtle()
score.penup()
score.hideturtle()
score.goto((300,400))
score.write('0', move=False, font=("Verdana",15, "normal"))


text = Turtle()
text.penup()
text.hideturtle()
text.goto((0,400))
text.write('Breakout Game', move=False, font=("Verdana",15, "normal"))


ball = Ball()
bubble_row = BubbleBox()
move_slider = True
onkeypress(slider.move_left, 'Left')
onkeypress(slider.move_right, 'Right')
game_is_on = True
scores =0

def hit_box(ball):
    global scores
    for each_turtle in bubble_row.turtles_list:
        if abs(each_turtle.xcor() - ball.xcor()) <= 20 and abs(each_turtle.ycor() - ball.ycor()) <= 20:
            each_turtle.clear()
            each_turtle.hideturtle()
            bubble_row.turtles_list.remove(each_turtle)
            print('turtle removed')
            scores += 1
            score.clear()
            score.write(scores, move=False, font=("Verdana", 15, "normal"))

        else:
            print('Nothing')


while game_is_on:
    ball.move_ball()
    hit_box(ball)
    y_diff = (slider.ycor() - ball.ycor()) * -1
    if slider.xcor() - 100 < ball.xcor() < slider.xcor() + 100 and y_diff <= 20:
        ball.move_up_down()
        ball.move_ball()
    elif ball.ycor() < -400:
        game_is_on = False
    elif ball.ycor() > 390:
        ball.move_up_down()
    elif ball.xcor() > 440 or ball.xcor() < -445:
        ball.move_left_right()

screen.mainloop()
