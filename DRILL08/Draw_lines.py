import turtle
import random
import math

def stop():
    turtle.bye()


def prepare_turtle_canvas():
    turtle.setup(1024, 768)
    turtle.bgcolor(0.2, 0.2, 0.2)
    turtle.penup()
    turtle.hideturtle()
    turtle.shape('arrow')
    turtle.shapesize(2)
    turtle.pensize(5)
    turtle.color(1, 0, 0)
    turtle.speed(100)
    turtle.goto(-500, 0)
    turtle.pendown()
    turtle.goto(480, 0)
    turtle.stamp()
    turtle.penup()
    turtle.goto(0, -360)
    turtle.pendown()
    turtle.goto(0, 360)
    turtle.setheading(90)
    turtle.stamp()
    turtle.penup()
    turtle.home()

    turtle.shape('circle')
    turtle.pensize(1)
    turtle.color(0, 0, 0)
    turtle.speed(50)

    turtle.onkey(stop, 'Escape')
    turtle.listen()


def draw_big_point(p):
    turtle.goto(p)
    turtle.color(0.8, 0.9, 0)
    turtle.dot(15)
    turtle.write('     '+str(p))


def draw_point(p):
    turtle.goto(p)
    turtle.dot(5, random.random(), random.random(), random.random())


def draw_line_basic(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)

    x1, y1  = p1
    x2, y2 = p2
    # y = ax + b ==> b = y - a*x
    # a = 
    a = (y2-y1)/(x2-x1)
    b = y1 - a*x1

    for x in range(x1,x2+1,10):
        y = a * x + b
        draw_point((x,y))

    draw_point(p2)

    pass


def draw_line(p1, p2):
    draw_big_point(p1)
    draw_big_point(p2)
    
    x1, y1  = p1
    x2, y2 = p2

    for i in range(0,100+1,2):
        t = i/100
        x = (1-t)*x1 + t*x2
        y = (1-t)*y1 + t*y2
        draw_point((x,y))

    draw_point(p2)
    pass

def draw_kite(size):
    for i in range(0,360,2):
        t = math.radians(i)
        
        x = math.cos(t)+(math.cos(t)**2*1.3)-0.8
        y = 1.5*math.sin(t)
        draw_point((x*size,y*size))

def draw_Peanut(size):
    for i in range(0,360,2):
        t = math.radians(i)
        
        p_constant = math.sqrt((math.cos(t)**2)+0.25*(math.sin(t)**2))
        x = p_constant*math.cos(t)
        y = p_constant*math.sin(t)
        draw_point((x*size,y*size))


def draw_R_triangle(size):
    for i in range(0,360,2):
        t = math.radians(i)
        p_constant = 2 + 0.3*math.cos(3*t)
        x = p_constant * math.cos(t)
        y = p_constant * math.sin(t)
        draw_point((x*size,y*size))

def draw_K_parametic(size, a, b, repeats,degree):
    for i in range(0,360*repeats,degree):
        t = math.radians(i)
        k = a/b
        x = (a-b)*math.cos(t) + b*math.cos(t*(k-1))
        y = (a-b)*math.sin(t) - b*math.sin(t*(k-1))
        draw_point((x*size,y*size))


prepare_turtle_canvas()

p1 = -200, 300
p2 = 200, 300

draw_K_parametic(10,6.5,10, 20, 6) # k = 0.65
draw_K_parametic(10,1,4,3,12) # k = 0.25
draw_R_triangle(100)
draw_Peanut(100)
draw_kite(100)
draw_line(p1,p2)
draw_line_basic(p1,p2)

# fill here

turtle.done()