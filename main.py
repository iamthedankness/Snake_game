import turtle as t
import time
from turtle import Turtle
from random import choice
screen=t.Screen()
screen.setup(width=600,height=600)
screen.title("Snake Game")
screen.bgcolor("black")
screen.tracer(0)
SCORE=0
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
up=90.0
down=270.0
left=180.0
right=0.0
def turn_left():
    if segments[0].heading() != right:
        segments[0].setheading(left)
def turn_right():
    if segments[0].heading() != left:
        segments[0].setheading(right)

def turn_up():
    if segments[0].heading() != down:
        segments[0].setheading(up)
def turn_down():
    if segments[0].heading() != up:
        segments[0].setheading(down)

numbers = [-280, -260, -240, -220, -200, -180, -160, -140, -120, -100, -80, -60, -40, -20, 0, 20, 40, 60, 80, 100, 120, 140, 160, 180, 200, 220, 240, 260, 280]
print(numbers)

starting_positions=[(0,0),(-20,0),(-40,0)]
segments=[]
snake=[]
def generate_random_cords():
    global snake
    c1=choice(numbers)
    c2 = choice(numbers)
    tup=(c1,c2)
    while tup in snake:
        generate_random_cords()

    return tup
food=Turtle("circle")
food.penup()
food.color("White")
food.goto(generate_random_cords())

for postion in starting_positions:
    new_segment=Turtle("square")
    new_segment.color("White")
    new_segment.penup()
    new_segment.goto(postion)
    segments.append(new_segment)
    snake.append((new_segment.xcor(),new_segment.ycor()))
def add_new_segment():
    segment=Turtle("square")
    segment.penup()
    segment.color("white")
    segment.goto(segments[-1].xcor(),segments[-1].ycor())
    segments.append(segment)
    snake.append((segment.xcor(),segment.ycor()))
screen.update()
game_on =True
while game_on:
    snake_length=-len(segments)+1
    while snake_length<=-1 :
        segments[snake_length].goto(snake[snake_length+1])
        snake[snake_length]=(segments[snake_length+1].xcor(),segments[snake_length+1].ycor())
        snake_length += 1
    segments[0].forward(20)
    snake[0]=(round(segments[0].xcor()),round(segments[0].ycor()))
    if snake[0][0]==food.xcor() and snake[0][1]==food.ycor():
        food.goto(generate_random_cords())
        add_new_segment()
        SCORE+=1
    if snake[0] in snake[1:] or snake[0][0]==-300 or snake[0][0]==300 or snake[0][1]==-300 or snake[0][1]==300:
        game_on=False
        print("game over")

    print(f"snake head x={snake[0][0]} and y={snake[0][1]}")
    print(f"food x={food.ycor()} and y={food.ycor()}")
    screen.listen()

    screen.onkeypress(turn_left,"a")

    screen.onkeypress(turn_right, "d")

    screen.onkeypress(turn_up,"w")

    screen.onkeypress(turn_down, "s")
    print(f"thi is heading {segments[0].heading()}")
    screen.update()
    time.sleep(0.1)




screen.exitonclick()