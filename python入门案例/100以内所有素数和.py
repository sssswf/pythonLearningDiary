sum = 2 #求和，1不是素数
for i in range(3, 100):
    for a in range(2, i):#对一个数挨个求模，判断是否为素数
        if i % a == 0:
            break
        elif a == i-1:#点睛之笔！
            sum += i
print(sum)

