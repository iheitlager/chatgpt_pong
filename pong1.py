# generated by ChatGPT on 2023-04-25 with some tweaks to make it a working game

import turtle
import time

# Set up the screen
width, height = 600, 400
screen = turtle.Screen()
screen.title("Pong Game")
screen.bgcolor("black")
screen.setup(width=width, height=height)

# Create the paddles and ball
left_paddle = turtle.Turtle()
left_paddle.shape("square")
left_paddle.color("white")
left_paddle.shapesize(stretch_wid=5, stretch_len=1)
left_paddle.penup()
left_paddle.goto(-250, 0)

right_paddle = turtle.Turtle()
right_paddle.shape("square")
right_paddle.color("white")
right_paddle.shapesize(stretch_wid=5, stretch_len=1)
right_paddle.penup()
right_paddle.goto(250, 0)

ball = turtle.Turtle()
ball.shape("circle")
ball.color("white")
ball.penup()
ball.goto(0, 0)
ball.dx = 5
ball.dy = 5

# Create the score variables
left_score = 0
right_score = 0

score = turtle.Turtle()
score.color("white")

# Create the score display
def turtle_start():
    score.penup()
    score.hideturtle()
    score.goto(0, 170)
    score.clear()
    score.write("Player 1: {}  Player 2: {}".format(left_score, right_score), align="center", font=("Courier", 16, "normal"))
    ball.goto(0, 0)

# Define the paddle movement functions
def left_paddle_up():
    y = left_paddle.ycor()
    y += 20
    left_paddle.sety(y)

def left_paddle_down():
    y = left_paddle.ycor()
    y -= 20
    left_paddle.sety(y)

def right_paddle_up():
    y = right_paddle.ycor()
    y += 20
    right_paddle.sety(y)

def right_paddle_down():
    y = right_paddle.ycor()
    y -= 20
    right_paddle.sety(y)

def exit_game():
    score.clear()
    score.write("Game Over!", align="center", font=("Courier", 16, "normal"))
    time.sleep(2)
    screen.bye    


# Bind the paddle movement functions to keys
screen.listen()
screen.onkeypress(left_paddle_up, "w")
screen.onkeypress(left_paddle_down, "s")
screen.onkeypress(right_paddle_up, "Up")
screen.onkeypress(right_paddle_down, "Down")
screen.onkeypress(exit_game, "x")

# Main game loop
turtle_start()
while True:
    # Move the ball
    ball.setx(ball.xcor() + ball.dx)
    ball.sety(ball.ycor() + ball.dy)

    # Check for wall collisions
    if ball.ycor() > 190 or ball.ycor() < -190:
        ball.dy *= -1

    # Check for paddle collisions
    if ball.xcor() > 240:
        if ball.distance(right_paddle) < 50:
            ball.dx *= -1
        else:
            left_score += 1
            turtle_start()
            time.sleep(2)

    if ball.xcor() < -240:
        if ball.distance(left_paddle) < 50:
            ball.dx *= -1
        else:
            right_score += 1
            turtle_start()
            time.sleep(2)


    # Check for game over
    if left_score == 5 or right_score == 5:
        exit_game()