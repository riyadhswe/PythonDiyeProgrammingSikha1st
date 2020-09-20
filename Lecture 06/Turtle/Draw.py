import turtle
turtle.color("Black")
turtle.speed(5)
counter = 0
while counter < 36:
    for i in range(4):
        turtle.forward(100)
        turtle.right(100)
    turtle.right(90)
    counter += 1
turtle.exitonclick()