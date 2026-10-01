from turtle import *

tracer(0)
screensize(600, 600)
k = 20
lt(90)

for _ in range(2):
    fd(21 * k)
    rt(90)
    fd(27 * k)
    rt(90)

penup()
fd(9 * k)
rt(90)
fd(10 * k)
lt(90)

pendown()

for _ in range(2):
    fd(86 * k)
    rt(90)
    fd(47 * k)
    rt(90)

penup()

for x in range(-40, 40): 
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(4)

exitonclick()