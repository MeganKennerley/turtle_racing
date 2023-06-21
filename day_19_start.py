""" Etchasketch """
# def f():
#     tim.forward(10)
#
# def b():
#     tim.backward(10)
#
# def l():
#     tim.left(10)
#
# def r():
#     tim.right(10)
#
# def c():
#     tim.clear()
#     tim.penup()
#     tim.home()
#     tim.pendown()
#
# screen.listen()
# screen.onkey(f, "w")
# screen.onkey(b, "s")
# screen.onkey(l, "a")
# screen.onkey(r, "d")
# screen.onkey(c, "c")


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
    michael_the_turtle = Turtle(shape="turtle")
    michael_the_turtle.penup()
    michael_the_turtle.color(colors[turtle])
    michael_the_turtle.goto(x=-230, y=y_positions[turtle])
    all_turtles.append(michael_the_turtle)

if user_bet:
    is_on = True

while is_on:

    for michael in all_turtles:
        if michael.xcor() > (230):
            is_on = False
            winning_color = michael.pencolor()
            if winning_color.lower() == user_bet.lower():
                print(f"You win! {winning_color.capitalize()} was the winner!")
            else:
                print(f"Sorry! You lost! {winning_color.capitalize()} was the winner!")
        random_distance = random.randint(0, 10)
        michael.forward(random_distance)



screen.exitonclick()