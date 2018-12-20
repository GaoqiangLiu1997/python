#-*- coding="UTF-8" -*-
# eval()传入一个纯数字字符串，会将这个字符串转换为数字返回
# str()传入数字将其转换为字符串类型返回

str1=input("请输入数据：\n")
print("初始数据类型是：")
print(type(str1))#验证str1初始数据类型

number1=eval(str1) #将str1经过eval函数转换赋值给number1
print("经过eval()转换的数据类型是：")
print(type(number1))#打印number1的数据类型

str2=str(number1) #将number1经过str函数转换赋值给str2
print("经过str()转换的数据类型是：")
print(type(str2))#打印str2的数据类型