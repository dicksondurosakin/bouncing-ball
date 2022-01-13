from turtle import Turtle

class Paddle(Turtle):
    def __init__(self):
        """Inherits from the turtle class and 
            create a 5 square paddle"""
        super().__init__()
        self.shape('square')
        self.setheading(90)
        self.penup()
        self.turtlesize(4,0.5)
        self.goto(0,-280)
        self.collision_distance = 30
        
        
    # def check_colision(self,ball):
    #     """checks if the paddle has made collision with the ball"""
    #     if self.distance(ball) < self.collision_distance:
    #         return True
    
    def move_paddle_right(self):
        """Function that moves the paddle to the right"""
        self.goto(self.xcor()+self.collision_distance,self.ycor())
    
    
    def move_paddle_left(self):
        """Function that moves the paddle to the left"""
        self.goto(self.xcor()-self.collision_distance,self.ycor())


    

