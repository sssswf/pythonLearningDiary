'''
获得用户输入的一个字符串，格式如下：
‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬‭M OP N
‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫‬其中，M和N是任何数字，OP代表一种操作，表示为如下四种：+, -, *, /（加减乘除）
‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬‮‬‫根据OP，输出M OP N的运算结果，统一保存小数点后2位。
‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‭‬‪‬‪‬‪‬‪‬‪‬‮‬‭‬‫‬‪‬‪‬‪‬‪‬‪‬‮‬‪‬‮‬‪‬‪‬‪‬‪‬‪‬注意：M和OP、OP和N之间可以存在多个空格，不考虑输入错误情况。
'''
'''
s = input()
for i in range(len(s)):
    if s[i] == '+':
        for i in range(len(s)):
            if s[i] != ' ' and s[i+1] == ' ':
                print(eval(s[0:i+1]))
                continue
            elif s[i] == ' ' and s[i+1] != ' ' and s[i+1] != '+':
                print(eval(s[i+1:]))
    elif s[i]=='-':
        print(eval(s[0]) - eval(s[-1]))
    elif s[i]=='*':
        print(eval(s[0]) * eval(s[-1]))
    elif s[i]=='/':
        print(eval(s[0]) / eval(s[-1]))
 '''
s = input()
print("{:.2f}".format(eval(s)))