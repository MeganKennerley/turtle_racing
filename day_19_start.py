from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)

colors = ["pink", "red", "yellow", "green", "blue", "purple"]
user_bet = screen.textinput(title="Make a bet", prompt=f"What colour turtle do you think will win?: "
                                                       f"({colors}) ")
y_positions = [-125, -75, -25, 25, 75, 125]
all_turtles = []
is_on = False

for turtle in range(0, 6):
    turtle = Turtle(shape="turtle")
    turtle.penup()
    turtle.color(colors[turtle])
    turtle.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(turtle)

if user_bet:
    is_on = True

while is_on:

    for turtle in all_turtles:
        if turtle.xcor() > (230):
            is_on = False
            winning_color = turtle.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You win! {winning_color.capitalize()} was the winner!")
            else:
                print(f"Sorry! You lost! {winning_color.capitalize()} was the winner!")
        random_distance = random.randint(0, 10)
        turtle.forward(random_distance)



screen.exitonclick()
