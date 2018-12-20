#-*- coding="UTF-8" -*-
# id()传入一个变量参数会返回这个变量的地址
# type()传入一个变量参数，会返回这个变量的数据类型

myStr1="A"
myNumber1=2018
myNumber2=2018

print(id(myStr1)) #print打印是内容的数据类型必须统一，全是数字或全是字符串
print(str(id(myNumber1))+";"+str(id(myNumber2))) #python是地址赋值形式，myNumber1与myNumber2的值相同，所以系统会把同一个地址赋值给他们

print(type(myStr1))
print(type(myNumber1))