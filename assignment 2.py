import time
import turtle
from turtle import Turtle
from random import randint

# window title
window = turtle.Screen()
window.title("Drawing Our Group Number")
window.bgcolor("grey")
window.screensize(800,740)
t=turtle.Turtle()


t.hideturtle()

# TURTLE 1 created and starts drawing a five
t1 = Turtle()
t1.pensize(5)
t1.speed(0)
t1.color("blue","orange")
t1.shape("turtle")
t1.up()
t1.goto(-60, 250)
t1.rt(180)
t1.begin_fill()
t1.pendown()
t1.fd(240)
t1.lt(90)
t1.fd(275)
t1.lt(90)
t1.fd(45)
t1.lt(64)
for i in range(309):
    t1.fd(0.7)
    t1.rt(0.5)
t1.fd(70)
for i in range(350):
    t1.fd(0.7)
    t1.rt(0.51)
t1.lt(90)
t1.fd(45)
t1.lt(90)
for i in range(449):
    t1.fd(0.9)
    t1.lt(0.4)
t1.fd(85)
for i in range(310):
    t1.fd(0.9)
    t1.lt(0.42)
t1.rt(131)
t1.fd(150)
t1.rt(89.7)
t1.fd(195)
t1.lt(90)
t1.fd(52)
t1.end_fill()# finishes drawing a five
t1.up()
t1.goto(-400, 370) #goes to the race starting point
t1.rt(90.1)
t1.pd()

# TURTLE 2 created and goes to the race starting point
t2 = Turtle()
t2.speed(0)
t2.color("orange")
t2.shape("turtle")
t2.up()
t2.goto(-400, 350)
t2.pd()


# TURTLE 3 created and goes to the race starting point
t3 = Turtle()
t3.speed(0)
t3.color("light green")
t3.shape("turtle")
t3.up()
t3.goto(-400, 330)
t3.pd()


# TURTLE 4 created  and starts drawing a nine
t4 = Turtle()
t4.pensize(5)
t4.speed(0)
t4.color("purple","light green")
t4.shape("turtle")
t4.up()
t4.setpos(60,130)
t4.pd()
t4.lt(90)
t4.begin_fill()
for i in range(360):
    t4.fd(1)
    t4.rt(0.5)

t4.fd(270)
for i in range(360):
    t4.fd(1)
    t4.rt(0.5)
t4.rt(90)
t4.fd(50)
t4.rt(90)
for i in range(200):
    t4.fd(1)
    t4.lt(0.9)
t4.fd(170)
t4.lt(140)
for i in range(274):
    t4.fd(0.87)
    t4.rt(0.5)
t4.fd(45)
t4.end_fill()
t4.up()
t4.color("purple","grey")
t4.setpos(110,130)
t4.pd()
t4.begin_fill()
for i in range(180):
    t4.fd(1)
    t4.rt(1)
t4.fd(20)
for i in range(180):
    t4.fd(1)
    t4.rt(1)
t4.fd(20)
t4.up()
t4.end_fill() # finishes drawing a nine
t4.up()
t4.goto(-400, 310) #goes to the race starting point
t4.rt(93)
t4.pd()

# TURTLE 5 created and goes to the race starting point
t5 = Turtle()
t5.speed(0)
t5.pensize(5)
t5.color("purple")
t5.shape("turtle")
t5.up()
t5.goto(340, 370)
t5.pd()
t5.rt(90)

# TURTLE 6 created and goes to the race starting point
t6 = Turtle()
t6.speed(0)
t6.color("light green")
t6.shape("turtle")
t6.up()
t6.goto(360, 370)
t6.pd()
t6.rt(90)

# TURTLE 7 created and goes to the race starting point
t7 = Turtle()
t7.speed(0)
t7.color("orange")
t7.shape("turtle")
t7.up()
t7.goto(380, 370)
t7.pd()
t7.rt(90)

# TURTLE 8 created and goes to the race starting point
t8 = Turtle()
t8.speed(0)
t8.pensize(5)
t8.color("blue")
t8.shape("turtle")
t8.up()
t8.goto(400, 370)
t8.pd()
t8.rt(90)

# TURTLE 9 created and goes to the race starting point
t9 = Turtle()
t9.speed(0)
t9.pensize(5)
t9.color("purple")
t9.shape("turtle")
t9.up()
t9.goto(400,-300)
t9.pd()
t9.rt(180)

# TURTLE 10 created and goes to the race starting point
t10 = Turtle()
t10.speed(0)
t10.color("light green")
t10.shape("turtle")
t10.up()
t10.goto(400,-320)
t10.pd()
t10.rt(180)

# TURTLE 11 created and goes to the race starting point
t11 = Turtle()
t11.speed(0)
t11.color("orange")
t11.shape("turtle")
t11.up()
t11.goto(400, -340)
t11.pd()
t11.rt(180)

# TURTLE 12 created and goes to the race starting point
t12 = Turtle()
t12.speed(0)
t12.pensize(5)
t12.color("blue")
t12.shape("turtle")
t12.up()
t12.goto(400, -360)
t12.pd()
t12.rt(180)

# TURTLE 13 created and goes to the race starting point
t13 = Turtle()
t13.speed(0)
t13.pensize(5)
t13.color("purple")
t13.shape("turtle")
t13.up()
t13.goto(-340, -360)
t13.pd()
t13.lt(90)

# TURTLE 14 created and goes to the race starting point
t14 = Turtle()
t14.speed(0)
t14.color("light green")
t14.shape("turtle")
t14.up()
t14.goto(-360, -360)
t14.pd()
t14.lt(90)

# TURTLE 15created and goes to the race starting point 
t15 = Turtle()
t15.speed(0)
t15.color("orange")
t15.shape("turtle")
t15.up()
t15.goto(-380, -360)
t15.pd()
t15.lt(90)

# TURTLE 16created and goes to the race starting point 
t16 = Turtle()
t16.speed(0)
t16.pensize(5)
t16.color("blue")
t16.shape("turtle")
t16.up()
t16.goto(-400, -360)
t16.pd()
t16.lt(90)

for i in range(200):  # The race starts as soon as all turltes have reached 
                      # the starting point , distance per move is determined by a
                      # random pick between 1 and 5 for all turtles
    t1.fd(randint(5,10))
    t2.fd(randint(5,10))
    t3.fd(randint(5,10))
    t4.fd(randint(5,10))
    t5.fd(randint(5,10))
    t6.fd(randint(5,10))
    t7.fd(randint(5,10))
    t8.fd(randint(5,10))
    t9.fd(randint(5,10))
    t10.fd(randint(5,10))
    t11.fd(randint(5,10))
    t12.fd(randint(5,10))
    t13.fd(randint(5,10))
    t14.fd(randint(5,10))
    t15.fd(randint(5,10))
    t16.fd(randint(5,10))
window.exitonclick()
window.mainloop() # End of program
