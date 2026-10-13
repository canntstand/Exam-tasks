from turtle import *

tracer(0)
screensize(1000, 1000)
k = 20
lt(90)

for _ in range(2):
    fd(20 * k)
    lt(270)
    fd(12 * k)
    rt(90)

penup()

fd(9 * k)
rt(90)
fd(7 * k)
lt(90)

pendown()

for _ in range(2):
    fd(13 * k)
    rt(90)
    fd(6 * k)
    rt(90)

penup()

for x in range(-20, 30):
    for y in range(-20, 30):
        goto(x * k, y * k)
        dot(4)

exitonclick()
