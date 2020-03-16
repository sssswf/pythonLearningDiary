# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
sale = pd.read_excel("C:/Temp/sale.xlsx",index_col='Day')
#绘制折线趋势图
#sale.plot(y=['Clothes', 'Shoes', 'Jeans', 'Hats'])
sale.plot.area(y=['Clothes', 'Shoes', 'Jeans', 'Hats'])
#绘制叠加区域图
plt.title("Sale 10days Trend",fontsize=18,fontweight='bold')
plt.xlabel('Day',fontweight='bold')
plt.ylabel('RMB',fontweight='bold')
plt.xticks(sale.index)
f = plt.gcf()#获取figure并调整图片区域的显示位置
f.subplots_adjust(left=0.125,top=0.9)
plt.tight_layout()#紧凑显示
plt.show()
