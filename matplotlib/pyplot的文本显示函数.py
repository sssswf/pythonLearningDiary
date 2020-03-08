# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
a = np.arange(10)
plt.plot(a,a*2)
plt.title("超市近期营业额概览",fontproperties='SimHei',fontsize=12)
plt.ylabel("营业额：万元",fontproperties='SimHei',fontsize=12)
plt.xlabel("天数：天",fontproperties='SimHei',fontsize=12)
plt.text(5,10,'突破10万元',fontproperties='SimHei',fontsize=12)
plt.annotate('5w', xy=(2.5,5), xytext=(1.5,8),
             arrowprops=dict(facecolor='black',shrink=0.1,width=2))
#用于设定箭头，xy表示箭头的位置，xytext表示文本的位置，shrink表示箭头周围有空隙
#plt.annotate(s, xy=arrow_crd, xytext=text_crd, arrowprops=dict)
plt.grid(True)
plt.savefig("pyplot的文本显示函数")
plt.show()

