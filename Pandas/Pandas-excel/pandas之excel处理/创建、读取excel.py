import pandas as pd
people = pd.DataFrame({'ID':[1,2,3],'Name':['a','s','d']})
people.to_excel('C:/Temp/people.xlsx')
people_copy = pd.read_excel('C:/Temp/people.xlsx')

