from matplotlib import pyplot as plt
import numpy as np
import matplotlib as mat
a = np.arange(10)
plt.plot(a,a*2)
mat.rcParams['font.family']='SimHei'
mat.rcParams['font.size']=20
plt.ylabel("纵轴",fontproperties='FangSong')
plt.xlabel("横轴")
plt.savefig("pyplot的中文显示")
plt.show()
