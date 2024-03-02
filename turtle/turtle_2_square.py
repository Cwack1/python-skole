import turtle as t

t.speed(2)
t.shape("turtle")

sider = 4
grader = 90
lengde = 150
for count in range(sider):
    t.forward(lengde)
    t.left(grader)

t.exitonclick()