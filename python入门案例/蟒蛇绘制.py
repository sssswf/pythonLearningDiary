#python 蟒蛇绘制
import turtle as t
t.setup(1000,300,200,200)
t.penup()
t.fd(-200)
t.pendown()
t.pensize(25)
t.pencolor(0.5,0.23,0.66)
t.seth(-40)
for i in  range(4):
    t.circle(50,80)
    t.circle(-50,80)
t.circle(50,80/2)
t.fd(50)
t.circle(20,180)
t.fd(30)
t.done()


