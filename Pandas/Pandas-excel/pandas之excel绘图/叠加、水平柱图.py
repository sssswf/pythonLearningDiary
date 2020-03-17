import pandas as pd
import matplotlib.pyplot as plt
stu = pd.read_excel("C:/Temp/stu.xlsx")
stu.sort_values(by='Total_grades',inplace=True,ascending=False)
#stu.plot.bar(x='Name',y=['Math_grades','English_grades'],stacked=True,color=['blue','orange'])
stu.plot.barh(x='Name',y=['Math_grades','English_grades'],stacked=True,color=['blue','orange'])
#plt.bar(stu.Name,stu.Total_grades)
plt.title("Students'grades",fontsize=18,fontweight='bold')
plt.xlabel('Grades',fontweight='bold')
plt.ylabel('Name',fontweight='bold')
f = plt.gcf()#获取figure并调整图片区域的显示位置
f.subplots_adjust(left=0.125,top=0.9)
plt.tight_layout()#紧凑显示
plt.show()