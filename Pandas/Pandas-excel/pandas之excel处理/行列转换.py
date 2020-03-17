# -*- coding: utf-8 -*-
import pandas as pd
worker = pd.read_excel("C:/Temp/worker.xlsx",index_col='ID')
table = worker.transpose()
print(table)
