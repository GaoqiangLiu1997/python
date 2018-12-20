#-*- coding="UTF-8" -*-
import  time

beginTime=time.time()
print("========================================================================")
print("                            九九乘法表")
print("========================================================================")
for i in range(1,10,1): #(1,10,1)起始值1,步长1，结束值9（不包含10）
    for j in range(1,i+1,1):
        temp=str(str(i)+"X"+str(j)+"="+str(format(i*j,"<2d"))) #format字符串格式化
        print(temp,end=("  "))
    print()
print("========================================================================")
print("                             完成打印")
print("========================================================================")
endTime=time.time()
timeCha=endTime-beginTime
print("用时："+str(format(timeCha,".4f"))+"秒")