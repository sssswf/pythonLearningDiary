'''
一年365天，“三天打鱼两天晒网”的工作模式，
工作的时候每天进步1%，休息的时候每天退步0.3%，
一年下来进步多少？ 5.700

如果想要达到和上述一样的效果，每天退步却是0.5%，那应该每天进步多少？
'''
def dayrun(dayup):
    daynow = 1
    daydown = 0.005
    for i in range(365):
        if i % 5 in [4,0]:
            daynow = daynow * (1 - daydown)
        else:
            daynow = daynow * (1 + dayup)
    return daynow
dayup = 0.01
while(dayrun(dayup) < 5.700):
    dayup = dayup + 0.001
print("dayup:{:.3f}".format(dayup))
