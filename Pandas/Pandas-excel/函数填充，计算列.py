# -*- coding: utf-8 -*-
import pandas as pd
student_grades = pd.read_excel("C:/Temp/student.xlsx")
student_grades.Math_grades += 2
student_grades.English_grades -= 3
student_grades.Total_grades = student_grades.Math_grades + student_grades.English_grades
student_grades = student_grades.set_index("ID")
student_grades.to_excel("C:/Temp/output_stu.xlsx")
print('done!')