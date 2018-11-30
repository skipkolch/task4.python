# -*- coding: utf-8 -*-
"""
Created on Thu Nov 29 21:14:02 2018

@author: skip_kolch
"""

import pandas as pd
import matplotlib.pyplot as plt
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

df = pd.read_csv('apple.csv', sep=',', encoding='latin1', parse_dates=['Date'], dayfirst=True, index_col='Date')

#task4.1
summ = df.groupby(df.index.weekday_name).Volume.sum()


plt.ylabel('Summ Volume')
summ.plot.bar()
plt.show()

#task4.2
average = df.resample('Y').Close.mean()
print(average)
