from turtle import *

tracer(0)
screensize(500, 500)
lt(90)
k = 20

for _ in range(4):
    fd(8 * k)
    rt(90)
    fd(8 * k)
    rt(90)

penup()

for x in range(-20, 20):
    for y in range(-20, 20):
        goto(x * k, y * k)
        dot(5)
        
exitonclick()