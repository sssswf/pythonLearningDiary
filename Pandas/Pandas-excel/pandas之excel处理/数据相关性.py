# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
pd.options.display.max_columns=10
house = pd.read_excel("C:/Temp/house.xlsx",index_col='ID')
print(house.corr())
#展示列之间的相关性
