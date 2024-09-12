import turtle
from apple import Apple
from snake import Snake
import time
apple = Apple(0,0,0.5)

snake = Snake((0, 0), "right")
turtle.listen()
turtle.onkey(snake.right, "Right")
turtle.onkey(snake.left, "Left")
turtle.onkey(snake.up, "Up")
turtle.onkey(snake.down, "Down")
while True:

    snake.move()
    time.sleep(0.5)
    if abs(snake.head.xcor() - apple.xcor())<15 and abs(snake.head.ycor() - apple.ycor()) < 15:
        apple.refresh()
        snake.extend()
        
        
    

turtle.mainloop()