# -*- coding: utf-8 -*-
import pandas as pd
stu_grades = pd.read_excel("C:/Temp/student.xlsx",sheet_name="stu_grades",index_col='Name')
stu_class = pd.read_excel("C:/Temp/student.xlsx",sheet_name="stu_class",index_col='Name')
table = stu_grades.join(stu_class,how='right').fillna(0)
#join默认采用index进行表的联合，也可通过 on 进行设置
#how用于确定是保留左表还是右表  fillna用于填充NaN
table[['Math_grades','English_grades','Total_grades']]=table[['Math_grades',
     'English_grades','Total_grades']].astype(int)
print(table)