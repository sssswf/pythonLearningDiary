# -*- coding: utf-8 -*-
import pandas as pd
pd.options.display.max_columns=777
stu = pd.read_excel("C:/Temp/student.xlsx",sheet_name="stu_grades")
temp = stu[['Math_grades','English_grades']]
row_sum = temp.sum(axis=1)
row_mean = temp.mean(axis=1)
stu['Total_grades'] = row_sum
stu['Average_grades'] = row_mean
col_mean = stu[['Math_grades','English_grades','Total_grades']].mean()
col_mean['Name'] = 'summary'
stu = stu.append(col_mean,ignore_index=True)
print(stu)