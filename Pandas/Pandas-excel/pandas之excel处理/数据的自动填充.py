# -*- coding: utf-8 -*-
import pandas as pd
from datetime import date,timedelta
def add_month(d,md):
    yd = md//12
    m = d.month + md % 12
    if m != 12:
        yd += m//12
        m = m%12
    return date(d.year + yd,m,d.day)
people = pd.read_excel('C:/Temp/people.xlsx',skiprows=3,usecols="C:F",dtype={'ID':str,'Sex':str,'Birth':str})
#skiprows用于跳过行,usecols用于规定列
#当单元格为空时，单元格默认为NaN
#当Serise存在NaN时，默认dtype为float64类型，因此在添加空单元格时需要注意类型
#此处通过读取时设置dtype将其全部转换为str类型
start = date(2020,1,1)
for i in people.index:
    people['ID'].at[i] = i+1
    people['Sex'].at[i] = 'boy' if i%2==0 else 'girl'   
    people['Birth'].at[i] =add_month(start,i) 
people = people.set_index('ID')
people.to_excel("C:/Temp/output.xlsx")