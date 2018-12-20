import  time

number1=time.time()#开始
sum=0
for i in range(90000099):
    sum=sum+i
print(sum)

number2=time.time()#结束

freetime=number2-number1
print(str(format(freetime,".2f"))+"秒")