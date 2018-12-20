#-*- coding="UTF-8" -*-
#使用ord（）与chr（）做单字符大写转换工具
while 1 : #设置一个死循环，让程序持续重复运行
    myStr = input("请输入单个字符：")
    asciimyStr = ord(myStr)
    if asciimyStr >= 65 and asciimyStr <= 90:
        print("您输入的是大写字母，它对应的小写字母是：", end=(" "))
        print(chr(asciimyStr + 32))
    elif asciimyStr >= 97 and asciimyStr <= 122:
        print("您输入的是小写字母，它对应的大写字母是：", end=(" "))
        print(chr(asciimyStr - 32))
    else:
        print("Error")
