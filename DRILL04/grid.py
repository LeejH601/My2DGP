import turtle
count = 0
width = 100
turtle.reset()
while (count < 6):
    point = (0,width * count)
    turtle.goto (point)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    count += 1
turtle.penup()
turtle.goto(0,0)
turtle.pendown()
turtle.left(90)
count = 0
while (count < 6):
    point = (width * count,0)
    turtle.goto (point)
    turtle.pendown()
    turtle.forward(500)
    turtle.penup()
    count += 1
