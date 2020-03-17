# -*- coding: utf-8 -*-
import pandas as pd
import matplotlib.pyplot as plt
house = pd.read_excel("C:/Temp/house.xlsx")
house.plot.scatter(x='Sqft_living',y='Price')
plt.show()
