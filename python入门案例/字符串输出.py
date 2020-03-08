s = input("str:")
num = input("num:")
if eval(num)==0:
    print(s)
elif eval(num)>0:
    for i in range(int(len(s)/2)):
        if i == 5:
            print(s[-1])
            break
        print(s[2*i],s[2*i+1])
elif eval(num)<0:
    for i in range(len(s)):
        print(s[i])
else:
    print("错误输入")