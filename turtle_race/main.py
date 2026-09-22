from turtle import Turtle,Screen
import random

my_screen=Screen()
my_screen.setup(height=500,width=500)
their_bet= my_screen.textinput(title="turtle game",prompt="Place a bet on which turtle will win")

positions =[ (-240,120),(-240,60),(-240,0),(-240,-190),(-240,-130)]
colors=["red","green","purple","yellow","orange"]
turtle_list=[]

is_on=True


for x in range(1,6):
    segment=Turtle()
    segment.penup()
    segment.shape("turtle")
    segment.color(colors[x-1])
    segment.goto(positions[x-1])
    turtle_list.append(segment)

while is_on:

    for each_turtle in turtle_list:
        random_distance = random.randint(0,10)
        each_turtle.forward(random_distance)
        if each_turtle.xcor() > 230:
            winner_color = each_turtle.fillcolor()
            if winner_color == their_bet:
                print(f"You got it correct {winner_color} won the race")
                is_on=False
            else:
                print(f"You got it wrong {winner_color} won the race")
                is_on=False

my_screen.exitonclick()