import random
import time
numpoint = 1000*1000
numcircle = 0.0
rcircle = 1.0
start = time.perf_counter()
for i in range(0,numpoint+1):
    x = random.random()
    y = random.random()
    if  pow(x*x+y*y,0.5) < rcircle:
        numcircle += 1
pi = 4 * (numcircle/numpoint)
print(pi)
print("运行时间：{:.2f}".format(time.perf_counter()-start))