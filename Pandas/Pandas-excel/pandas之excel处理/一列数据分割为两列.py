# -*- coding: utf-8 -*-
#将Name分割为first name和last name
import pandas as pd
people = pd.read_excel("C:/Temp/people.xlsx",index_col='ID')
df = people.Name.str.split(expand=True)
#expand为True时可在分割后直接扩充为多列
people['first_name'] = df[0]
people['last_name'] = df[1]
#创建新的列时，不能使用a.b的方式
people = people.drop("Name",axis=1)
#drop默认删除行索引，删除列索引时，需要添加axis=1
print(people)

