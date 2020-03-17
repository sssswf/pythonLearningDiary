# -*- coding: utf-8 -*-
import pandas as pd
student = pd.read_excel("C:/Temp/stu_output.xlsx")
student = student.loc[student.Math_grades.apply(lambda a:a>=80)].loc[student.English_grades.apply(lambda a:a>=80)]
print(student)
