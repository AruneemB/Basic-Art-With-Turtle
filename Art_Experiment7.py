#Create 6 rows of colored squares

#Import turtle
import turtle

#Set background to black
turtle.bgcolor('black')
shelly = turtle.Turtle()

#Set the order of colors
colors = ['red', 'green', 'blue', 'orange', 'purple', 'yellow'] #Picks the order of colors of for the 6 squares

#Create 6 rows of colored squares
for b in range(6): #Repeats the following 6 times
#Make a row of colored squares
    for n in range(6): #Repeats the following 6 times
        shelly.color(colors[n])
        for i in range(4): #Creates squares
            shelly.forward(20)
            shelly.left(90)
        shelly.penup()
        shelly.forward(30)
        shelly.pendown()
    shelly.penup()
    shelly.backward(180)
    shelly.left(90)
    shelly.forward(30)
    shelly.right(90)
    shelly.pendown()

#Hide turtle
shelly.hideturtle()
