# -*- coding: utf-8 -*-
"""
Created on Sun May 19 07:22:54 2019

@author: KIIT
"""

#https://pythonprogramming.net/yahoo_finance_replacement

# Importing library
import numpy as np
import matplotlib.pyplot as plt
import urllib
import matplotlib.dates as mdates
import datetime as datetime
from matplotlib import style

stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source = urllib.request.urlopen(stock_price_url).read().decode().split('\n')
close=[]# Closing price 
datas=[]
dates=[]
openp=[]
for row in source[1:]:
    list1 = row.split(',')
    datas.append(list1)
for i in range(len(datas)):
    datas[i][0]=datetime.datetime.strptime(datas[i][0],'%Y-%m-%d')
    dates.append(datas[i][0])
    close.append(float(datas[i][4]))  
    openp.append(float(datas[i][1]))
    
    
# Data Visualisation
fig = plt.figure()
ax1 = plt.subplot2grid((1,1),(0,0))
#ax1.plot_date(dates,close,'-',label='Price')

#ax1.plot([],[],label='Loss',linewidth = 5,color='r',alpha = 0.5)
#ax1.plot([],[],label='Gain',linewidth = 5,color='g',alpha = 0.5)

ax1.plot(dates,close)
ax1.plot(dates,openp)
# Used to point the line
#ax1.axhline(close[5],color='red',linewidth=3)



#ax1.fill_between(dates,close,close[0],where=[i>close[0] for i in close],facecolor='b',alpha=1)
#ax1.fill_between(dates,close,close[0],where=[i<close[0] for i in close],facecolor='r',alpha=0.5)

for label in ax1.xaxis.get_ticklabels():
    label.set_rotation(45)
#ax1.grid(True)#,color='r',linestyle='-',linewidth=5)
# Color the labels
#ax1.xaxis.label.set_color('c')
#ax1.yaxis.label.set_color('r')

# Set the ticks here i.e draw a line parallel to x axis on the values in list
ax1.set_yticks([0,100,500,1005])

# Working with axis

ax1.spines['left'].set_color('c')
ax1.spines['right'].set_visible(False)
ax1.spines['top'].set_visible(False)
ax1.spines['left'].set_linewidth(5)

ax1.tick_params(axis='x',colors='#f06215')
ax1.tick_params(axis='y',colors='#f06215')

                
#Styles in matplotlib like css in html
print(plt.style.available)
style.use('fast')
'''
'bmh', 'classic', 'dark_background', 'fast', 'fivethirtyeight', 'ggplot',
 'grayscale', 'seaborn-bright', 'seaborn-colorblind', 'seaborn-dark-palette', 'seaborn-dark', 
 'seaborn-darkgrid', 'seaborn-deep', 'seaborn-muted', 'seaborn-notebook', 'seaborn-paper',
 'seaborn-pastel', 'seaborn-poster', 'seaborn-talk', 'seaborn-ticks', 'seaborn-white',
 'seaborn-whitegrid'
, 'seaborn', 'Solarize_Light2', 'tableau-colorblind10', '_classic_test'
'''




plt.legend()
plt.xlabel('Dates')
plt.ylabel('Price')
plt.title('Stock closing price')
plt.subplots_adjust(left = 0.09,bottom=0.20,right=0.94,top=0.94,wspace = 0.2,hspace = 0)
plt.show()
