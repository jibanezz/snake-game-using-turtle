import turtle
import random
class Apple(turtle.Turtle):
    def __init__(self, x, y, size):
        super().__init__()
        self.speed(0)
        self.penup()
        self.goto(x, y)
        self.shape("circle")
        self.color("green")
        self.radius = size / 2
        self.growing_speed = 0.05
    
    def grow(self):
        self.radius += self.growing_speed
        self.shapesize(self.radius)
    def refresh(self):
        self.goto(random.randint(-200,200), random.randint(-200,200))
        
    
if __name__ == "__main__":
    apple  = Apple(0,0,0.5)
    turtle.mainloop()