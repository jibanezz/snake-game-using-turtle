import turtle
from apple import Apple
from snake import Snake

apple = Apple(0,0,0.5)

snake = Snake((0, 0), "right")
turtle.listen()
turtle.onkey(snake.right, "Right")
turtle.onkey(snake.left, "Left")
turtle.onkey(snake.up, "Up")
turtle.onkey(snake.down, "Down")
while True:

    snake.move()
    if snake.head.distance(apple.pos) < 15:
        apple.refresh()
        
    

turtle.mainloop()