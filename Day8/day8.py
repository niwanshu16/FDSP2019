# -*- coding: utf-8 -*-
"""
Created on Wed May 15 17:05:29 2019

@author: KIIT
"""

from bs4 import BeautifulSoup
import requests


source = requests.get('https://www.icc-cricket.com/rankings/mens/team-rankings/t20i').text

soup = BeautifulSoup(source,"lxml")



right_table =  soup.find('table',class_='table')

print(right_table)

A=[]
B=[]
C=[]
D=[]

for row in right_table.findAll('tr'):
    cells = row.findAll('td')
    if len(cells) == 5:
        A.append(cells[1].text.strip())
        B.append(cells[2].text.strip())
        C.append(cells[3].text.strip())
        D.append(cells[2].text.strip())
        
import pandas as pd
from collections import OrderedDict

col_name = ['Index','Country','Weighted Matches','Rating','Rating Points']

col_data = OrderedDict(zip(col_name,[A,B,C,D]))

df = pd.DataFrame(col_data)
df.to_csv('rating_t20.csv')


# Download pic
import urllib.request
r = requests.get('http://forsk.in/images/Forsk_logo_bw.png')

with open('forskjpg.png','wb') as fp:
    fp.write(r.content)
    
#https://bidplus.gem.gov.in/bidlists
    
from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup 
from pandas import DataFrame 
url = "https://bidplus.gem.gov.in/bidlists"
browser = webdriver.Chrome('D:\programs\python\Programs\Day8\selenium\chromedriver.exe')
browser.get(url)
A=[]
B=[]
C=[]
D=[]
E=[]
F=[]
for i in range(1,11):
    A.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[1]/p[1]/a').text)
    B.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[1]/span').text)
    C.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[3]/p[2]').text)
    D.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[2]/p[2]/span').text)
    E.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[1]/span').text)
    F.append(browser.find_element_by_xpath('//*[@id="pagi_content"]/div['+str(i)+']/div[4]/p[2]/span').text)
    #get_click.click()

# Turn into csv file 
column = ['BidNo','Item(s)','Department name and address','Quantity','StartDate','EndDate']

col_data = OrderedDict(zip(column,[A,B,C,D,E,F]))
df = pd.DataFrame(col_data)
df.to_csv('BidData.csv')



html_page = browser.page_source


soup = BeautifulSoup(html_page,"lxml")   
data = soup.findAll('div',class_='col-block')
print(data.find('p'))


import requests
url = "https://bidplus.gem.gov.in/bidlists"
source = requests.get(url).text

soup = BeautifulSoup(source,"lxml")

data = soup.find('div')

right_div = soup.findAll('div',class_='border block')

A=[]
B=[]
C=[]
D=[]
E=[]

for row in right_div:
    print(row.text)
    