from turtle import Turtle, Screen
import turtle
import random
screen = Screen()
turtle.colormode(255)

jim = Turtle()

jim.shape("classic")
jim.speed("fastest")
jim.penup()
jim.hideturtle()
# jim.color("red")
color_list = [(26, 108, 164), (193, 38, 81), (237, 161, 50), (234, 215, 86), (227, 237, 229), (223, 137, 176), (143, 108, 57), (103, 197, 219), (21, 57, 132), (205, 166, 30), (213, 74, 91), (238, 89, 49), (142, 208, 227)]


# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r, g, b)
#     return random_color

    #
    # jim.clearstamp(20)
jim.setheading(225)
jim.fd(300)
jim.setheading(0)
num_of_dots = 100

for dot_count in range(1, num_of_dots + 1):
    jim.dot(20, random.choice(color_list))
    jim.forward(50)
    if dot_count % 10 == 0:
        jim.setheading(90)
        jim.fd(50)
        jim.setheading(180)
        jim.fd(500)
        jim.setheading(0)

# for _ in range(10):
#     # jim.color(random_color())
#     jim.fd(20)
#     jim.penup()
#     jim.fd(20)
#     jim.pendown()



screen.exitonclick()