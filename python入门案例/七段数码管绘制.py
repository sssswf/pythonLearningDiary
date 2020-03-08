import turtle,time
def drawGap():#让线段之间有间隔感
    turtle.penup()
    turtle.fd(5)
def drawLine(draw):
    drawGap()
    turtle.pendown() if draw else turtle.penup()
    #if else在同一行的表示方法
    #输入的参数draw为布尔值，为真时，画一条真实的线，为假时，画一条不存在的线
    turtle.fd(40)
    drawGap()
    turtle.right(90)
def drawNumber(num):#不同数字画不同的线
    drawLine(True) if num in [2,3,4,5,6,7,8,9] else drawLine(False)
    drawLine(True) if num in [0, 1, 3, 4, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if num in [0, 2, 3, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if num in [0, 2, 6, 8] else drawLine(False)
    turtle.left(90)
    drawLine(True) if num in [0,4, 5, 6, 8, 9] else drawLine(False)
    drawLine(True) if num in [0,2, 3, 5, 6, 7, 8, 9] else drawLine(False)
    drawLine(True) if num in [0,1,2, 3, 4, 7, 8, 9] else drawLine(False)
    turtle.left(180)
    turtle.penup()#为绘制后续数字确定位置
    turtle.fd(20)#为绘制后续数字确定位置

def drawDate(date):#date为日期，格式为‘%Y-%m=%d+’
    turtle.pencolor("red")
    for i in date:
        if i == '-':
            turtle.write('年',font=('Arial',18,'normal'))
            turtle.pencolor('green')
            turtle.fd(40)
        elif i == '=':
            turtle.write('月', font=('Arial', 18, 'normal'))
            turtle.pencolor('blue')
            turtle.fd(40)
        elif i == '+':
            turtle.write('日',font=('Arial', 18, 'normal'))
        else:
            drawNumber(eval(i))
def main():
    turtle.setup(800,350)
    turtle.penup()
    turtle.fd(-300)
    turtle.pensize(5)
    drawDate(time.strftime("%Y-%m=%d+",time.gmtime()))
    turtle.hideturtle()
    turtle.done()
main()