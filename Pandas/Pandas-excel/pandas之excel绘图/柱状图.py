# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
stu = pd.read_excel("C:/Temp/stu.xlsx")
stu.sort_values(by='Total_grades',inplace=True,ascending=False)
stu.plot.bar(x='Name',y='Total_grades',color='blue')
#plt.bar(stu.Name,stu.Total_grades)
plt.title("Students'grades",fontsize=18)
plt.xlabel('Name')
plt.ylabel('Total_grades')
plt.tight_layout()
plt.show()
