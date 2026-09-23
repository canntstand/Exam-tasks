from turtle import *

screensize(500, 500)
lt(90)
tracer(0)
k = 18

for _ in range(5):
    fd(29 * k)
    rt(90)
    fd(27 * k)
    rt(90)

penup()

fd(3 * k)
rt(90)
fd(9 * k)
lt(90)

pendown()

for _ in range(5):
    fd(72 * k)
    rt(90)
    fd(95 * k)
    rt(90)

penup()

for x in range(-20, 40):
    for y in range(-20, 40):
        goto(x * k, y * k)
        dot(3)

exitonclick()
