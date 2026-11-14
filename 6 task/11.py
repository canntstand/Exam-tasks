from turtle import *

tracer(0)
left(90)
k = 40
screensize(2000, 2000)

rt(315)
for _ in range(7):
    fd(12 * k)
    rt(45)
    fd(6 * k)
    rt(135)

penup()

for x in range(-40, 40):
    for y in range(-40, 40):
        goto(x * k, y * k)
        dot(3)

exitonclick()
