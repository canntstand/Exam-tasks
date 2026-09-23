# не знаю как посчитать точки, нарисовать получилось
from turtle import *

screensize(1000, 1000)
k = 15
tracer(0)
lt(90)

rt(90)
for _ in range(3):
    rt(45)
    fd(10 * k)
    rt(45)

rt(315)
fd(10 * k)

for _ in range(2):
    rt(90)
    fd(10 * k)
    
penup()

for x in range(-20, 40):
    for y in range(-20, 40):
        goto(x * k, y * k)
        dot(3)
        
exitonclick()