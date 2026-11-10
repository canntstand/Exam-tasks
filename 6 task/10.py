from turtle import *

tracer(0)
screensize(4000, 4000)
left(90)
k = 5

rt(315)
for _ in range(7):
    fd(72 * k)
    rt(45)
    fd(43 * k)
    rt(135)

penup()

for x in range(-90, 90):
    for y in range(-90, 90):
        goto(x * k, y * k)
        dot(3)

exitonclick()
