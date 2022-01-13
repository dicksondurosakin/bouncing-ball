from tkinter import font
from bricks import Brick
from paddle import Paddle
from ball import Ball
from turtle import Turtle, Screen

screen = Screen()
screen.setup(700, 600)

# Creating all the neccessary in the screen
screen.tracer(0)
ball = Ball()
brick = Brick()
only_paddle = Paddle()
screen.tracer(1)

# Move the paddle
screen.onkey(only_paddle.move_paddle_right,"Right")
screen.onkey(only_paddle.move_paddle_left,"Left")
screen.listen()

# Creating a turtle that will write on the screen
writing_turtle = Turtle()
writing_turtle.ht()
writing_turtle.penup()
writing_turtle.color('red')
writing_turtle.goto(-150,0)

while True:
    ball.move()
    # check if the ball has made contact with the walls
    if ball.xcor() >= 320 or ball.xcor() < -330:
        ball.wall_bounce()

    # check if it hits any of the bricks 
    for i in brick.bricks:
        if i.distance(ball) < 25:
            screen.tracer(0)
            i.goto(1000,1000)
            brick.bricks.remove(i)
            screen.tracer(1)

    # check if ball has made contact with paddle
    if ball.ycor() < -260 and only_paddle.distance(ball) <= 40:
        ball.paddle_and_up_bounce()
    # check if ball has made contact with top bar
    if ball.ycor() >= 290:
        ball.paddle_and_up_bounce()
    # check if the player has lost 
    if ball.ycor() < -280:
        writing_turtle.write("GAME OVER",font=('Segeo ui',40,'normal'))
        break
    if brick.bricks == []:
        writing_turtle.color('green')
        writing_turtle.goto(-200,0)
        writing_turtle.write("GENIUS YOU WIN",font=('Segeo ui',40,'normal'))
        break



screen.mainloop()