from  turtle import Turtle
LOCATIONS=[(0,0),(-20,0),(-40,0)]
MOVE_DISTANCE=20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0



class SnakeBody:
    def __init__(self):
        super().__init__()
        self.turtle_list = []
        self.create_snake()
        self.head=self.turtle_list[0]


    def create_snake(self):
        for location in LOCATIONS:
            self.add_segment(location)

    def add_segment(self,location):
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.color("white")
        new_turtle.shape("square")
        new_turtle.goto(location)
        self.turtle_list.append(new_turtle)

    def extend(self):
        self.add_segment(self.turtle_list[-1].position())


    def snake_movement(self):
        for number in range(len(self.turtle_list)-1,0,-1):
           new_x= self.turtle_list[number-1].xcor()
           new_y=self.turtle_list[number-1].ycor()
           self.turtle_list[number].goto(new_x,new_y)
        self.turtle_list[0].forward(MOVE_DISTANCE)

    # up_function
    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    # down_function
    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    # left_function
    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    # right_function
    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
