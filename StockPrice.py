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
    
    
    
    
stock_price_url = 'https://pythonprogramming.net/yahoo_finance_replacement'
source = urllib.request.urlopen(stock_price_url).read().decode().split('\n')
close=[]# Closing price 
datas=[]
dates=[]
for row in source[1:]:
    list1 = row.split(',')
    datas.append(list1)
for i in range(len(datas)):
    datas[i][0]=datetime.strptime(datas[i][0],'%Y-%m-%d')
    dates.append(datas[i][0])
    close.append(float(datas[i][4]))  
plt.plot_date(dates,close)
plt.xlabel('Dates')
plt.ylabel('Price')
plt.title('Stock closing price')
#plt.legend()
plt.show()
