import time
import turtle
from turtle import Turtle
from random import randint

# window title
window = turtle.Screen()
window.title("Turtle Race")
turtle.bgcolor("violet")
turtle.color("white")
turtle.speed(0)
turtle.penup()
turtle.setpos(-140, 200)
turtle.write("Turtle Race", font=("Arial", 40, "bold"))
turtle.penup()

stamp_size = 20
square_size = 15
finish_line = 200

turtle.color("black")
turtle.shape("square")
turtle.shapesize(square_size / stamp_size)
turtle.penup()

for i in range(20):
    turtle.setpos(finish_line, (150 - (i * square_size * 1)))
    turtle.stamp()


turtle.hideturtle()

# TURTLE 1
turtle1 = Turtle()
turtle1.speed(0)
turtle1.color("blue")
turtle1.shape("turtle")
turtle1.penup()
turtle1.goto(-250, 100)
turtle1.pendown()


# TURTLE 2
turtle2 = Turtle()
turtle2.speed(0)
turtle2.color("yellow")
turtle2.shape("turtle")
turtle2.penup()
turtle2.goto(-250, 50)
turtle2.pendown()

# TURTLE 3
turtle3 = Turtle()
turtle3.speed(0)
turtle3.color("red")
turtle3.shape("turtle")
turtle3.penup()
turtle3.goto(-250, 0)
turtle3.pendown()


# TURTLE 4
turtle4 = Turtle()
turtle4.speed(0)
turtle4.color("white")
turtle4.shape("turtle")
turtle4.penup()
turtle4.goto(-250, -50)
turtle4.pendown()

for i in range(145):
    turtle1.forward(randint(1,5))
    turtle2.forward(randint(1,5))
    turtle3.forward(randint(1,5))
    turtle4.forward(randint(1,5))


turtle.exitonclick()

turtle.mainloop()
