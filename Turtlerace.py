from turtle import *
from random import randint
speed(20)
penup()
goto(-140,140)
for step in range(21):
    if(step==20):
        pensize(5)
        pencolor('purple')
        write('  Finish')
    pensize(1)
    pencolor('black')   
    right(90)
    forward(20)
    pendown()
    forward(150)
    penup()
    backward(170)
    left(90)
    forward(20)


pensize(5)
pencolor('purple')
right(90)
forward(20)
pendown()
forward(150)
penup()
backward(170)
left(90)
forward(20)

b1=Turtle()
b1.color('red')
b1.shape('turtle')
b1.penup()
b1.goto(-160,100)


b2=Turtle()
b2.color('green')
b2.shape('turtle')
b2.penup()
b2.goto(-160,60)


b3=Turtle()
b3.color('blue')
b3.shape('turtle')
b3.penup()
b3.goto(-160,20)


b4=Turtle()
b4.color('yellow')
b4.shape('turtle')
b4.penup()
b4.goto(-160,-20)

for turn in range(210):
    b1.forward(randint(1,3))
    b2.forward(randint(1,3))
    b3.forward(randint(1,3))
    b4.forward(randint(1,3))
    
    
