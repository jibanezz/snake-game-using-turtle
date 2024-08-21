import turtle
class Snake(turtle.Turtle):
    def __init__(self, start_position, start_direction):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("square")
        self.color("pink")
        self.direction = start_direction
        self.segments = [self]
        self.create_segments()
        self.head = self.segments[0]
        self.goto(start_position)
    
    def create_segments(self):
        for _ in range(len(self.segments) - 1):
            new_segment = self.clone()
            new_segment.goto(0, 0)
            self.segments.append(new_segment)
    
    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            x, y = self.segments[index - 1].xcor(), self.segments[index - 1].ycor()
            self.segments[index].goto(x, y)
        self.head.forward(1)
    
    def up(self):
        if self.direction!= "down":
            self.direction = "up"
            self.head.setheading(90)
    
    def down(self):
        if self.direction!= "up":
            self.direction = "down"
            self.head.setheading(270)

    def left(self):
        if self.direction!= "right":
            self.direction = "left"
            self.head.setheading(180)
    
    def right(self):
        if self.direction!= "left":
            self.direction = "right"
            self.head.setheading(0)
    
if __name__ == "__main__":
    
    
    snake = Snake((0, 0), "right")
    turtle.listen()
    turtle.onkey(snake.right, "Right")
    turtle.onkey(snake.left, "Left")
    turtle.onkey(snake.up, "Up")
    turtle.onkey(snake.down, "Down")
    while True:
    
        snake.move()
    
    turtle.mainloop()