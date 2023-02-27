import turtle
import random


tim = turtle.Turtle()
tim.speed(0) #max speed
tim.width(5)

colors = ['red','blue','green','purple','yellow','orange','black']

def up():
    tim.setheading(90) #sets turtle pointing upwards. 
    tim.forward(100)

def down():
    tim.setheading(270)  
    tim.forward(100)

def right():
    tim.setheading(0) 
    tim.forward(100)

def left():
    tim.setheading(180)  
    tim.forward(100)

def clickleft(x,y):
    tim.color(random.choice(colors)) #random selects a colour from the list

def clickright(x,y):
    tim.stamp() #literally samps the turtle down

#turtle has a lot of events that basically lets the user interact. So moving the mouse or
#hitting a key

turtle.listen() #lets the program know that we are now listening for events to happen
#turtle.onclick(clickleft,1) happens when the user actually clicks the turtle. 
turtle.onscreenclick(clickleft,1) #1 for left 2 for middle 3 for right
turtle.onscreenclick(clickright,3)

turtle.onkey(up,"Up")#calls the function up when the 'Up error' key is pressed
turtle.onkey(down,"Down")
turtle.onkey(left,"Left")
turtle.onkey(right,"Right")



turtle.done()