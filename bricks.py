from turtle import Turtle

class Brick(Turtle):
    """Creating the Bricks that the ball are going to hit"""
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.bricks = []
        self.x_position = -300
        self.y_position = 200
        self.x_position2 = -300
        self.y_position2 = 160

        for i in range(48):
            if i == 12:
                self.x_position = -300
                self.y_position = 160
            if i == 24:
                self.x_position = -300
                self.y_position = 120
            if i == 36:
                self.x_position = -300
                self.y_position = 80
            new_brick = Turtle("square")
            new_brick.penup()
            new_brick.shapesize(1,2)
            new_brick.goto(self.x_position ,self.y_position)
            self.bricks.append(new_brick)
            self.x_position += 50
        

