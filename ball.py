from turtle import Turtle
import random

class Ball(Turtle):
    """Creating the Ball for the game"""
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.distance = 5
        self.x_distance = 0
        self.y_distance = -10
        self.option = [-10,10,-5,5]

    def move(self):
        """move the ball down"""
        self.penup()
        # self.hideturtle()
        self.setheading(-90)
        self.goto(self.xcor()+self.x_distance,self.ycor()+self.y_distance)

    def paddle_and_up_bounce(self):
        if self.x_distance == 0:
            self.x_distance = random.choice(self.option)
        self.y_distance *= -1

    def wall_bounce(self):
        self.x_distance *= -1