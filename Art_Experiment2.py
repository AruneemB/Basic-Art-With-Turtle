#Create a house using starter code

#Import turtle
import turtle

#Set background to Navy Blue
turtle.bgcolor('navyblue')
shelly = turtle.Turtle()

#Start to create house
#Make first big yellow square for base structure of house
shelly.begin_fill() #Start the fill of color
shelly.color('yellow')
for i in range(4):
    shelly.forward(100)
    shelly.left(90)
shelly.end_fill() #End the fill of color
shelly.penup()
shelly.goto(-20,100) #Move the turtle to next area
shelly.pendown()

#Make a red triangle roof
shelly.begin_fill() #Start the fill of the roof
shelly.color('red')
shelly.left(60)
for i in range(2):
    shelly.forward(140)
    shelly.right(120)
shelly.forward(140)
shelly.end_fill() #End the fill of color for roof

#Create first window
shelly.penup()
shelly.goto(25,80) #Move to window position
shelly.pendown()
shelly.begin_fill() #Start filling window color
shelly.color('gray')
for i in range(4):
    shelly.forward(20)
    shelly.left(90)
shelly.end_fill() #End filling window color

#Create second window
shelly.penup()
shelly.goto(95,80) #Move to window position
shelly.pendown()
shelly.begin_fill() #Start filling window color
shelly.color('gray')
for i in range(4):
    shelly.forward(20)
    shelly.left(90)
shelly.end_fill() #End filling window color

#Create door under space between windows
shelly.penup()
shelly.goto(60,46)
shelly.pendown()
shelly.begin_fill() #Start filling door color
shelly.color('white')
for i in range(2):
    shelly.forward(20)
    shelly.left(90)
    shelly.forward(45)
    shelly.left(90)
shelly.end_fill() #End filling door color

#Hide the turtle when finished
shelly.hideturtle()
