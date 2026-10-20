from turtle import *

screensize(1000, 1000)
tracer(0)
k = 50
lt(90)

for _ in range(7):
    fd(10 * k)
    rt(120)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(4)

exitonclick()