import random
import turtle
from turtle import Turtle, Screen
is_on = False
screen = Screen()
screen.setup(width=500,height=400)
user_bet = screen.textinput(title="Make your bet!",prompt="Which turtle will win the race? Enter color:")
colors=["red","orange","yellow","green","blue","purple"]
y_position = [-80,-50,-20,10,40,70]
all_turtles = []
for turtle_index in range(0,6):
    my_turtle = Turtle("turtle")
    my_turtle.color(colors[turtle_index])
    my_turtle.penup()
    my_turtle.goto(x=-230,y=y_position[turtle_index])
    all_turtles.append(my_turtle)
if user_bet:
    is_on =True
while is_on:
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            is_on =False
            winning_color = turtle.pencolor()
            if winning_color == user_bet:
                print(f"You win! {winning_color} turtle is win")
            else:
                print(f"You fault! {winning_color} turtle is win")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)
screen.mainloop()