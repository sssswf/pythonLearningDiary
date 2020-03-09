# -*- coding: utf-8 -*-
from matplotlib import pyplot as plt
import numpy as np
N = 20
theta = np.linspace(0.0,2 * np.pi,N,endpoint=False)
#根据起止数据a,b等间距地填充size个数据，形成数组，endpoint=False时表示不包含b；
radii = 10 * np.random.rand(N)
width = np.pi / 4 * np.random.rand(N)

#plt.polar(theta, r)
#theta：每个标记所在射线与极径的夹角
#r：每个标记到原点的距离
ax = plt.subplot(111,projection = 'polar')
bars = ax.bar(theta,radii,width = width,bottom=0.0)

for r,bar in zip(radii,bars):
    bar.set_facecolor(plt.cm.viridis(r / 10.))
    bar.set_alpha(0.5)
plt.savefig("pyplot极坐标图的绘制")
plt.show()
