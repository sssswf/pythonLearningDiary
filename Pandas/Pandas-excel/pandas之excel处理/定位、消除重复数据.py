# -*- coding: utf-8 -*-
import pandas as pd
worker = pd.read_excel("C:/Temp/worker.xlsx")
#数据定位
dupe = worker.duplicated(subset='Worker_num')
dupe = dupe[dupe]
print(worker.iloc[dupe.index])

#数据消除
#worker.drop_duplicates(subset='Worker_num',inplace=True,keep='first')
#subset用于选择列，keep用于选择保留的重复部分，last保留后面重复部分
#print(worker)