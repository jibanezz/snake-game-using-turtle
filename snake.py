import turtle

# Snake class to handle all snake-related behavior
class Snake(turtle.Turtle):
    def __init__(self, start_position, start_direction):
        super().__init__()
        self.speed(0)
        self.penup()
        self.shape("square")
        self.color("pink")
        self.direction = start_direction
        self.segments = [self]
        self.head = self.segments[0]
        self.goto(start_position)

    # Move the snake in the current direction
    def move(self):
        for index in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[index - 1].xcor()
            new_y = self.segments[index - 1].ycor()
            self.segments[index].goto(new_x, new_y)

        # Move the head in the current direction
        if self.direction == "up":
            self.head.setheading(90)
        elif self.direction == "down":
            self.head.setheading(270)
        elif self.direction == "left":
            self.head.setheading(180)
        elif self.direction == "right":
            self.head.setheading(0)
        
        self.head.forward(20)  # Moves the snake head by 20 units

    # Snake movement controls
    def up(self):
        if self.direction != "down":  # Prevent the snake from moving in the opposite direction
            self.direction = "up"

    def down(self):
        if self.direction != "up":
            self.direction = "down"

    def left(self):
        if self.direction != "right":
            self.direction = "left"

    def right(self):
        if self.direction != "left":
            self.direction = "right"

    # Add a new segment to the snake
    def add_segment(self):
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("grey")
        new_segment.penup()
        # Place the new segment at the last position of the tail
        new_segment.goto(self.segments[-1].xcor(), self.segments[-1].ycor())
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment()


# Main game loop to run the game continuously
def game_loop(snake):
    snake.move()  # Call snake's move function to make it move in the current direction
    turtle.ontimer(lambda: game_loop(snake), 100)  # Calls the game_loop every 100 ms (adjust for speed)


if __name__ == "__main__":
    # Set up the screen
    screen = turtle.Screen()
    screen.title("Snake Game")
    screen.bgcolor("black")
    screen.setup(width=600, height=600)

    # Create the snake object
    snake = Snake((0, 0), "right")

    # Listen for keyboard events to control the snake
    turtle.listen()
    turtle.onkey(snake.right, "Right")
    turtle.onkey(snake.left, "Left")
    turtle.onkey(snake.up, "Up")
    turtle.onkey(snake.down, "Down")

    # Start the game loop
    game_loop(snake)

    turtle.mainloop()  # Keep the window open
