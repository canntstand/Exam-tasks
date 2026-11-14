from turtle import *

tracer(0)
k = 200
screensize(2000, 2000)
left(90)

begin_fill()
for _ in range(6):
    fd(31 * k)
    rt(60)
end_fill()

penup()

canvas = getcanvas()
cnt = 0

for x in range(-100, 100):
    for y in range(-100, 100):
        if canvas.find_overlapping(x * k, y * k, x * k, y * k) == (5,):
            cnt += 1

print(cnt)
