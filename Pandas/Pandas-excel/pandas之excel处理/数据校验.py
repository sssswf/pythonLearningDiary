# -*- coding: utf-8 -*-
import pandas as pd
def grades_check(df):
    try:
        assert 0<=df.Math_grades<=100 and 0<=df.English_grades<=100
        #assert（断言）用于判断一个表达式，在表达式条件为 false 的时候触发异常。
    except:
        print(f'#{df.Name} has invalid grades')
        #print字符串前面加f表示格式化字符串，加f后可以在字符串里面使用用花括号括起来的变量和表达式
stu = pd.read_excel("C:/Temp/student.xlsx",sheet_name='stu_grades')
stu.apply(grades_check,axis=1)
#df.apply()可以传入自定义的函数,axis=1表示一行一行进行校验
