import turtle as t

t.speed(2)
t.shape("turtle")

sider = 8
lengde = 110
for count in range(sider):
    t.forward(lengde)
    t.left(360 / sider)

t.exitonclick()