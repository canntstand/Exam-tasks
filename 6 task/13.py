from turtle import *

tracer(0)
screensize(2000, 2000)
left(90)
k = 30

rt(90)

for _ in range(7):
    rt(45)
    fd(11 * k)
    rt(45)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(4)
        
exitonclick()

#113