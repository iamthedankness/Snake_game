import snake
import turtle as t
import time
from turtle import Turtle
from random import choice

from snake import Snake

screen=t.Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
#TODO

# snake=[]
# def start():
#     x=20
#     y=0
#     for i in range(3):
#         new_turtle=t.Turtle(shape="square")
#         new_turtle.color("white")
#         new_turtle.teleport(x,y)
#         snake.append(new_turtle)
#         x-=20
#
# start()

sake= Snake()
sake.move()



screen.exitonclick()