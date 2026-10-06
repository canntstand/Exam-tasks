from turtle import *

tracer(0)
screensize(1000, 1000)
k = 20
lt(90)

for _ in range(2):
    fd(13 * k)
    rt(90)
    fd(18 * k)
    rt(90)
    
penup()

fd(5 * k)
rt(90)
fd(9 * k)
lt(90)

pendown()

for _ in range(2):
    fd(11 * k)
    rt(90)
    fd(7 * k)
    rt(90)
    
penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(4)

exitonclick()