#import turtle
import turtle
shelly = turtle.Turtle()

#set bacground to black
turtle.bgcolor('black')

#change shelly color to gray
shelly.color('gray')

#loop to make the circle art
for i in range(36): #loop puts the pen up, moves it forward, performs nested loop, and finally goes back, repeating 36 times
    shelly.penup()
    shelly.forward(200)
    for n in range(6): #nested loop creates a circle and goes backward 6 times
        shelly.pendown()
        shelly.circle(5)
        shelly.penup()
        shelly.backward(20)
    shelly.backward(80)
    shelly.right(10)
shelly.hideturtle() #hides turtle when finished
