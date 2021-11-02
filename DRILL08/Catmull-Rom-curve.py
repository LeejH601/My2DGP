import numpy
from line import *

count = 0

def catmull(p0, p1, p2, p3, div_p = 100):

    p0, p1, p2, p3 = map(numpy.array,[p0,p1,p2,p3])

    alpha = 0.5

    t0 = 0
    t1 = set_tj(t0,p0,p1,alpha)
    t2 = set_tj(t1,p1,p2,alpha)
    t3 = set_tj(t2,p2,p3,alpha)

    t = numpy.linspace(t1,t2,div_p)

    t = t.reshape(len(t),1)

    A1 = (t1-t)/(t1-t0)*p0 + (t-t0)/(t1-t0)*p1
    A2 = (t2-t)/(t2-t1)*p1 + (t-t1)/(t2-t1)*p2
    A3 = (t3-t)/(t3-t2)*p2 + (t-t2)/(t3-t2)*p3

    B1 = (t2-t)/(t2-t0)*A1 + (t-t0)/(t2-t0)*A2
    B2 = (t3-t)/(t3-t1)*A2 + (t-t1)/(t3-t1)*A3

    C = (t2-t)/(t2-t1)*B1 + (t-t1)/(t2-t1)*B2

    return C

def points_of_Catmull(point):
    size = len(point)


    catmull_points = []
    for i in range(size-3):
        C = catmull(point[i],point[i+1],point[i+2],point[i+3],50)
        catmull_points.extend(C)

    return catmull_points



def set_tj(ti, pi, pj, alpha):
    xi, yi = pi
    xj, yj = pj
    return (((xj-xi)**2+(yj-yi)**2)**0.5)**alpha + ti

def draw_catmull(c_points,point_list):
    # global count
    for p in point_list:
        # count += 1
        draw_big_point(p)
        # turtle.write('point'+str(count))
    for c in c_points:
        x, y = c
        draw_point((x,y))

def draw_curve_3_points(p1, p2, p3):

    x1, y1 = p1; x2, y2 = p2; x3, y3 = p3
    
    for i in range(0,100,2):
        t = i/100
        x = (2*t**2-3*t+1)*x1 + (-4*t**2+4*t)*x2 + (2*t**2-t)*x3
        y = (2*t**2-3*t+1)*y1 + (-4*t**2+4*t)*y2 + (2*t**2-t)*y3
        draw_point((x,y))

    draw_point(p3)

def draw_curve_4_points(p1, p2, p3, p4):
    draw_big_point(p1)
    draw_big_point(p2)
    draw_big_point(p3)
    draw_big_point(p4)

    # draw p1-p2
    for i in range(0, 50, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p1[0]+(-4*t**2+4*t)*p2[0]+(2*t**2-t)*p3[0]
        y = (2*t**2-3*t+1)*p1[1]+(-4*t**2+4*t)*p2[1]+(2*t**2-t)*p3[1]
        draw_point((x, y))
    draw_point(p2)

    # draw p2-p3
    for i in range(0, 100, 2):
        t = i / 100
        x = ((-t**3 + 2*t**2 - t)*p1[0] + (3*t**3 - 5*t**2 + 2)*p2[0] + (-3*t**3 + 4*t**2 + t)*p3[0] + (t**3 - t**2)*p4[0])/2
        y = ((-t**3 + 2*t**2 - t)*p1[1] + (3*t**3 - 5*t**2 + 2)*p2[1] + (-3*t**3 + 4*t**2 + t)*p3[1] + (t**3 - t**2)*p4[1])/2
        draw_point((x, y))
    draw_point(p3)

    # draw p3-p4
    for i in range(50, 100, 2):
        t = i / 100
        x = (2*t**2-3*t+1)*p2[0]+(-4*t**2+4*t)*p3[0]+(2*t**2-t)*p4[0]
        y = (2*t**2-3*t+1)*p2[1]+(-4*t**2+4*t)*p3[1]+(2*t**2-t)*p4[1]
        draw_point((x, y))
    draw_point(p4)

if __name__ == '__main__':
    prepare_turtle_canvas()

    p1 = x1, y1 = random.randint(-100,300),random.randint(100,300)
    p2 = x2, y2 = random.randint(-300,-100), random.randint(100,300)
    p3 = x3, y3 = random.randint(-300,-100), random.randint(-300,-200)
    p4 = x4, y4 = random.randint(200,400), random.randint(-400,-300)
    p5 = x5, y5 = 0,0
    p6 = x6, y6 = random.randint(-300,-100), random.randint(100,300)
    p7 = x7, y7 = random.randint(-300,-100), random.randint(-300,-200)
    p8 = x8, y8 = random.randint(200,400), random.randint(-400,-300)

    point_list = [p1,p4,p3,p2,p5]

    c_points = points_of_Catmull(point_list)

    draw_catmull(c_points,point_list)
    last_points = []
    last_points.append(point_list[0])
    size = len(point_list)
    for i in range(size-3,size):
        last_points.append(point_list[i])
    
    draw_curve_4_points(p3,p2,p5,p1)
    
    # draw_curve_3_points(p2,p5,p1)

    turtle.done()
