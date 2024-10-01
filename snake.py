import turtle as t
import time
from turtle import Turtle
from random import choice
screen=t.Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
UP=90
DOWN=270
LEFT=180
RIGHT=0
starting_positions = [(0, 0), (-20, 0), (-40, 0)]


class Snake:

    def __init__(self):
        self.segments = []
        self.snake = []
        self.start()

    def start(self):
        for postion in starting_positions:
            new_segment = Turtle("square")
            new_segment.color("White")
            new_segment.penup()
            new_segment.goto(postion)
            self.segments.append(new_segment)
            self.snake.append((new_segment.xcor(), new_segment.ycor()))
    def move(self):
        game_on = True
        while game_on:
            snake_length = -len(self.segments) + 1
            while snake_length <= -1:
                self.segments[snake_length].goto(self.snake[snake_length + 1])
                self.snake[snake_length] = (self.segments[snake_length + 1].xcor(), self.segments[snake_length + 1].ycor())
                snake_length += 1
            self.segments[0].forward(20)
            self.snake[0] = (round(self.segments[0].xcor()), round(self.segments[0].ycor()))




