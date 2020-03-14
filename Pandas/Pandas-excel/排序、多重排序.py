# -*- coding: utf-8 -*-
import pandas as pd
student = pd.read_excel("C:/Temp/output_stu.xlsx",index_col="ID")
#只按照总分排序
#student.sort_values(by='Total_grades',inplace=True,ascending=False)
#按照每个班级进行总分由高到低排序
student.sort_values(by=['Class','Total_grades'],inplace=True,ascending=[True,False])
student.to_excel("C:/Temp/stu_output.xlsx")

