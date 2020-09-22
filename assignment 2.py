import turtle
wn = turtle.Screen()             # Set up the window and its attributes
wn.bgcolor("grey")


turtmain = turtle.Turtle()           # create turtmain and set some attributes
turtmain.color("purple")
turtmain.pensize(2)

turthidden = turtle.Turtle() #create turthidden and set some attributes
turthidden.color("orange")
        
turtmain.left(90)   #begining of a cube drawing , main drawing
turtmain.forward(200)                 
turtmain.left(90)
turtmain.forward(450)
turtmain.left(90)
turtmain.forward(200)
turtmain.left(90) 
turtmain.forward(450) 
turtmain.left(30)  
turtmain.forward(300) 
turtmain.left(60)
turtmain.forward(200)
turtmain.left(90) 
turtmain.forward(450)
turtmain.left(30)  
turtmain.forward(300) 
turtmain.goto(0,200)
turtmain.left (180)  
turtmain.forward(300) 
turtmain.penup()
turtmain.home () #end of main drawing


turthidden.penup()   #begining of drawing of hidden detaild of the main drawing
turthidden.left(30)
turthidden.forward(300)
turthidden.pendown()               
turthidden.left(150)
turthidden.forward(450)
turthidden.left(30)
turthidden.forward(300)
turthidden.penup()
turthidden.left(180)
turthidden.forward(300)
turthidden.left(60)
turthidden.pendown()
turthidden.forward(200)  #end of the drawing of hidden details

wn.exitonclick()