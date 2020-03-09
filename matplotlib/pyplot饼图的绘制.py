# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
plt.title("学校人员构成比例",fontproperties='Kaiti',fontsize=12)
labels = 'Student','Teacher','Service','Manager'
#设置每部分的内容
sizes = [80,10,6,4]
#设置对应部分的比例
explode = (0.1,0,0,0)
#设置对应部分的“脱离”程度
plt.pie(sizes,explode=explode,labels=labels,autopct='%.1f%%',shadow=False,startangle=180)
#绘制饼图的函数，autopct设置比例显示的样式，shadow用于设置阴影，默认为False
plt.axis('equal')
#设置饼图的形状，此处为圆形
plt.savefig("pyplot饼图的绘制")
plt.show()

