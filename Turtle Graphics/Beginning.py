import turtle #basic graphics tool 

tim = turtle.Turtle()

tim.color("purple") #colour of turtle.
tim.pensize(5) #the size of the lines that the turtle will draw. 
tim.shape('arrow') #what the icon looks like: 'arrow''turtle''circle''square''triangle'

#this will create a basic purple square
tim.penup()
tim.backward(200)
tim.pendown()
for x in range(4):
    tim.forward(100)
    tim.left(90)

#this will create a green triangle
tim.color('green')
tim.penup()
tim.forward(300)
tim.pendown()
tim.left(45)
tim.forward(100)
tim.right(90)
tim.forward(100)
tim.right(135)
tim.forward(140)

#turtle.exitonclick()
turtle.done() # MUST have this or the screen will close. 
