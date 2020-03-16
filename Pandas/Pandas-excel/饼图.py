# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
school = pd.read_excel("C:/Temp/school.xlsx",index_col='title')
school['number'].plot.pie(startangle=90)
plt.title("School",fontsize=18)
plt.tight_layout()
plt.show()
