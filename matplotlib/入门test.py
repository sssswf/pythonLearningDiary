# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
plt.subplot(2,1,1)
#（行，列，选定区域）
#在全局绘图区域中创建一个分区体系，并定位到一个子绘图区域
plt.plot([0,2,4,6,8],[12,10,9,5,14])
#只有一个输入列表或数组时，默认为y轴，x轴为索引值
#plt.plot(x,y)当有两个以上参数时，按照X轴和Y轴顺序绘制数据点
#当绘制多条曲线时，各条曲线的x不能省略
plt.axis([0,10,0,16])
#用来确定x,y轴的边界值
plt.ylabel("ylabel")
#用于y轴的补充说明
plt.savefig("入门test")
#保存为图片，默认为png格式，可以通过dpi修改输出质量
plt.show()
