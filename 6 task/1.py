import turtle as t

t.screensize(2000, 2000)
t.left(90)
t.tracer(0)
k = 15


for i in range(4):
    t.fd(16 * k)
    t.right(90)
    t.fd(18 * k)
    t.right(90)

t.penup()

t.right(90)
t.fd(10 * k)
t.left(90)
t.fd(10 * k)

t.pendown()

for i in range(4):
    t.fd(15 * k)
    t.right(90)

t.penup()

t.fd(1 * k)
t.left(90)
t.fd(1)
t.right(90)

t.pendown()

for i in range(7):
    t.fd(12 * k)
    t.right(90)

t.penup()

for x in range(-20, 40):
    for y in range(-20, 40):
        t.goto(x * k, y * k)
        t.dot(5)

t.exitonclick()
