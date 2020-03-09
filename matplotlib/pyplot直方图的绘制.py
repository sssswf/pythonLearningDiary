from matplotlib import pyplot as plt
import numpy as np
np.random.seed(0)
mu,sigma = 100,20 #设置均值和标准差
a = np.random.normal(mu,sigma,size=100)
'''
np.random.normal(loc=0.0, scale=1.0, size=None)
用于生成高斯分布的概率密度随机数
loc：float
    此概率分布的均值（对应着整个分布的中心centre）
scale：float
    此概率分布的标准差（对应于分布的宽度，scale越大越矮胖，scale越小，越瘦高）
size：int or tuple of ints
    输出的shape（默认为None，只输出一个值）
'''
plt.hist(a,bins=30,histtype='stepfilled',color='b',density=True)
'''
plt.hist()y用于绘制直方图，以下是它的属性及说明
属性           说明                   类型
x              数据                 数值类型 
bins          条形数                  int 
color         颜色                "r","g","y","c" 
density     是否以密度的形式显示       bool 
range       x轴的范围              数值元组（起，终） 
bottom      y轴的起始位置            数值类型 
histtype     线条的类型         "bar":方形，"barstacked":柱形,<br />"step":"未填充线条"<br />"stepfilled":"填充线条" 
align          对齐方式           "left":左，"mid":中间，"right":右 
orientation   orientation      "horizontal":水平，"vertical":垂直 
log       单位是否以科学计术法         bool

'''
plt.title("Histogram")
plt.savefig("pyplot直方图的绘制")
plt.show()