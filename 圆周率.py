import  random
import  time

jishu1=0
jishu2=0
beginTime=time.time()
X=6666666
print("正在计算请稍后：",end=(" "))
for i in range(X):
    x = random.random()
    y = random.random()
    d = (x ** 2 + y ** 2) ** 0.5
    jishu1 = jishu1 + 1
    if d >= 0 and d <= 1:
        jishu2 = jishu2+ 1
    if jishu1 == X // 100*10 :
        print("10%",end=(" "))
    if jishu1 == X // 100*20 :
        print("20%",end=(" "))
    if jishu1 == X // 100*30 :
        print("30%",end=(" "))
    if jishu1 == X // 100*40 :
        print("40%",end=(" "))
    if jishu1 == X // 100*50 :
        print("50%",end=(" "))
    if jishu1 == X // 100*60 :
        print("60%",end=(" "))
    if jishu1 == X // 100*70 :
        print("70%",end=(" "))
    if jishu1 == X // 100*80 :
        print("80%",end=(" "))
    if jishu1 == X // 100*90 :
        print("90%",end=(" "))
cirAr=jishu2/jishu1*1*4
print("100%")
endTime=time.time()
timeCha=endTime-beginTime
print("圆周率约等于：",end=(" "))
print(format(cirAr,"1.2f"))
munite = timeCha  // 60
second = timeCha % 60
print("共计算了："+str(int(munite))+"分"+str(int(second))+"秒\n")