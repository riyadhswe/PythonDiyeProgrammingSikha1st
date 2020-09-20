import turtle
turtle.shape("turtle")
turtle.speed(1)
for i in range(100):
    for i in range(5):
        turtle.forward(10)
        turtle.left(30)

    for i in range(16):
        turtle.forward(10)
        turtle.right(30)


turtle.exitonclick()