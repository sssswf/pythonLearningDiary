# -*- coding: utf-8 -*-
import pandas as pd
A = pd.Series([1,2,3],index=[1,2,3],name="A")
B = pd.Series([10,20,30],index=[1,2,3],name="B")
C = pd.Series([100,200,300],index=[1,2,3],name="C")
#D = pd.DataFrame({A.name:A,B.name:B,C.name:C},index=[1,2,3])
D = pd.DataFrame([A,B,C])
D.to_excel("C:/Temp/output.xlsx")
print("done!")