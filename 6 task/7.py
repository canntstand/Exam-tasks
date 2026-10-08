from turtle import *
from math import *

tracer(0)

screensize(1000, 1000)

k = 20

lt(90)
fd(15 * k)

rt(90)
fd(3 * k)

rt(45)
fd((5 * sqrt(2) - 5) * k)

for _ in range(3):
    fd(5 * k)
    rt(45)

lt(45)
fd((5 * sqrt(2) - 5) * k)

lt(135)
bk(3 * k)

penup()
fd(8 * k)
pendown()

for _ in range(8):
    fd(6 * k)
    lt(45)

penup()

for x in range(-20, 40):
    for y in range(-20, 40):
        goto(x * k, y * k)
        dot(4)

exitonclick()