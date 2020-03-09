from matplotlib import pyplot as plt
import numpy as np
#面向对象绘制散点图
ax = plt.subplot()
#创建一个类似于画布的对象
ax.plot(10*np.random.randn(100),10*np.random.randn(100),'o')
ax.set_title("Simple Scatter")
plt.savefig("pyplot散点图的绘制")
plt.show()