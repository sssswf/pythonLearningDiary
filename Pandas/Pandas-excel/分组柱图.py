# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
stu = pd.read_excel("C:/Temp/stu.xlsx")
stu.sort_values(by='Math_grades',inplace=True,ascending=False)
stu.plot.bar(x='Name',y=['Math_grades','English_grades'],color=['blue','orange'])
#plt.bar(stu.Name,stu.Total_grades)
plt.title("Students'grades",fontsize=18,fontweight='bold')
plt.xlabel('Name',fontweight='bold')
plt.ylabel('Grades',fontweight='bold')
ax = plt.gca()#获取axis并调整x轴上的内容，使其旋转45°
ax.set_xticklabels(stu.Name,rotation=45,ha='right',fontweight='bold')
f = plt.gcf()#获取figure并调整图片区域的显示位置
f.subplots_adjust(left=0.125,top=0.9)
plt.tight_layout()#紧凑显示
plt.show()

