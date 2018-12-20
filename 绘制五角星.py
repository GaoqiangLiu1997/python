#-*- coding=UTF-8 -*-
import turtle
def  fiveStar():  # 定义一个函数fiveStar()，用于控制画笔前进与转向
    turtle.forward(200)          #画笔前进200
    turtle.right(144)            #画笔右转144度


def setPenSize():
    size = input("请输入画笔宽度，后回车确认开始绘制五角星：\n") # 输入语句，返回一个字符串类型
    size = eval(size)             # 将字符串转换为实数
    turtle.pensize(size)          # 设置画笔的宽度

def pencolor():
    pencolor1 = input("请输入画笔颜色，颜色有 red blue black green：\n")

    if pencolor1 != "red":
        if pencolor1 != "blue":
            if pencolor1 != "black":
                if pencolor1 != "green":
                     print("不存在此颜色!!!!!!!!!!!!!!")
                     pencolor()
    turtle.color(pencolor1)


setPenSize()
pencolor()


turtle.begin_fill()#开始填充
for i in range(5): #调用fiveStar()
    fiveStar()
turtle.color("red")#填充颜色
turtle.end_fill() #结束填充
turtle.hideturtle() #隐藏画笔箭头


turtle.done()

