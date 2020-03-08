# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
a = np.arange(10)
#生成一个0~9的ndarray数组
plt.plot(a,a*0.5,'b--.',a,a,':*',a,a*1.5,' +')
plt.savefig("多条曲线绘制")
plt.show()