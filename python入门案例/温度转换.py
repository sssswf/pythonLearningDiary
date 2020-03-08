#温度转换实例
tempstr = input("请输入一个带符号的数值：")#F\f表示华式温度  C\c表示摄氏度
if tempstr[-1] in ['F','f']:#如果输入是华式温度
    C = (eval(tempstr[0:-1])-32)/1.8
    '''索引和切片，索引分为正索引和负索引，
    正索引以第一个字符（0）开始，负索引以最后一个字符（-1）开始；
    切片是指取字符串中的一段，[x:y],包含x，但不包含y；
    eval()函数用于去掉字符或字符串的引号'''
    print("对应的摄氏温度为{:.2f}C".format(C)) #print函数的格式化
elif tempstr[-1] in ['C','c']:#当输入为摄氏度时
    F = eval(tempstr[0:-1])*1.8+32
    print("对应的华式温度为{:.2f}".format(F))
else:
    print("输入格式错误")