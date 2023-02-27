import turtle
import random
from sys import exit

bob = turtle.Turtle()

colors = ['red','blue','green','purple','yellow','orange','black']

#set color
bob.color('red','blue') #first color is outline, second color is fill
bob.pensize(5)
exit()

#basic filled shape
#bob.setpos(-200,50) #x and y coordinates
bob.speed(10)
for x in range(10):
    rand1 = random.randrange(-300,300)
    rand2 = random.randrange(-300,300)
    bob.color(random.choice(colors), random.choice(colors))
    bob.penup()
    bob.setpos(rand1,rand2)
    bob.pendown()
    bob.begin_fill()
    bob.circle(random.randrange(0,80))
    bob.end_fill()

turtle.done()