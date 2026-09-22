from snake import SnakeBody
from food import FoodMaster
from  turtle import Screen
from score_board import Scoreboard
import  time



my_screen =Screen()
my_screen.tracer(0)
my_screen.setup(width=500,height=500)
my_screen.title("snake game")
my_screen.bgcolor("black")


my_snake=SnakeBody()
snake_food=FoodMaster()
score_board=Scoreboard()

game_on=True




#control snake movement
my_screen.listen()
my_screen.onkey(key="Up",fun=my_snake.up)
my_screen.onkey(key="Down",fun=my_snake.down)
my_screen.onkey(key="Left",fun=my_snake.left)
my_screen.onkey(key="Right",fun=my_snake.right)



while game_on:
    my_screen.update()
    time.sleep(0.1)
    #snake movement
    my_snake.snake_movement()
    if my_snake.head.distance(snake_food)<15:
        snake_food.change_position()
        score_board.increase_score()
        my_snake.extend()
    if my_snake.head.xcor()>=245 or my_snake.head.xcor()<=-245 or my_snake.head.ycor()>=245 or my_snake.head.ycor()<=-245:
        score_board.game_over()
        game_on=False

    for turtle in my_snake.turtle_list[1:]:
     if my_snake.head.distance(turtle)<10:
            score_board.game_over()
            game_on=False





my_screen.mainloop()