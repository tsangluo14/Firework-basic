import turtle
import time
import random
fw=turtle.Turtle()
fw.hideturtle()
sc=turtle.Screen()
sc.bgcolor('black')
sc.tracer(0)

for i in range(200):
    scale=random.uniform(0.1,1.5)
    nlines=random.randint(6,15)
    color=random.choice(['cyan','purple','pink','teal','green','red','orange','gold'])
    fw.pencolor(color)
    fw.pensize(3)
    total=100*scale
    gap=10*scale
    while total-gap>0:
        for i in range(nlines):
            fw.pu();fw.fd(gap);fw.pd()
            fw.fd(total-gap)
            fw.pu();fw.bk(total);fw.pd()
            fw.rt(360/nlines)
        fw.rt(180/nlines)
        for i in range(nlines):
            fw.pu();fw.fd(gap/2);fw.pd()
            fw.fd(total/2-gap/2)
            fw.pu();fw.bk(total/2);fw.pd()
            fw.rt(360/nlines)
        fw.lt(180/nlines)
        sc.update()
        fw.clear()
        total*=1.05
        gap*=1.2
        time.sleep(0.01)
    fw.clear()
    time.sleep(0.05)
    
sc.update()