# -*- coding: utf-8 -*-
"""
Created on Fri May 24 10:43:13 2019

@author: KIIT
"""

import pandas as pd
dataset = pd.read_csv('Baltimore_City_Employee_Salaries_FY2014.csv')
import numpy as np
# Remove the dollar sign and assign it as a float


# Groupby Job title

grouped = dataset.groupby(['JobTitle'])['AnnualSalary']
aggregated1 = grouped.agg([np.sum , np.mean , np.std , np.size , np.min , np.max])

# Sort by salary
pd.set_option('display.max_rows',10000000)
output = aggregated1.sort_values(by = ['amax'],ascending = 0,inplace = False)
print(output.head(15))

# How many employees are in each job title

df = dataset.groupby(['JobTitle'])[' Name']
aggregated = df.agg([np.sum])
for i in range(len(aggregated)):
    aggregated['sum'][i] = len(aggregated['sum'][i].split(','))

output = aggregated.sort_values(by = ['sum'], ascending = 0)
output = output.head(15)

from matplotlib.ticker import FormatStrFormatter

myplot = output.plot(kind = 'bar' , title='Baltimore Total Annual Salary by Job Title - 2014')
myplot.set_ylabel('$')
myplot.yaxis.set_major_formatter(FormatStrFormatter('%d'))
'''myplot.savefig.format('Baltimore Total Annual Salary by Job Title.jpg')

This line doesnt work so we have to change the 
object of axessubplot to figure to use savefig
'''
fig = myplot.get_figure()
fig.savefig('Baltimore Total Annual Salary by Job Title.jpg')