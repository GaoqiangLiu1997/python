#-*- coding="UTF-8" -*-
import time
def jiecheng(n):
    jc=n
    temp =n
    for i in range(1,n):
        temp = temp - 1
        jc=jc*temp
    return  jc
while -1 :
    beginTime=time.time()
    n = eval(input("请输入一个数：\n"))
    print("该数的阶乘是：%d" % (jiecheng(n)))
    endTime=time.time()
    timeCha = endTime - beginTime
    munite = timeCha // 60
    second = timeCha % 60
    print("共计算了：" + str(int(munite)) + "分" + str(int(second)) + "秒\n")