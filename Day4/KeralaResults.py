# -*- coding: utf-8 -*-
"""
Created on Fri May 17 08:29:58 2019

@author: KIIT
"""
# http://court.mah.nic.in/courtweb/index_eng.php
from  selenium import webdriver
from time import sleep
from bs4 import BeautifulSoup 
from pandas import DataFrame 

url = "http://keralaresults.nic.in/sslc2019duj946/swr_sslc.htm"
browser = webdriver.Chrome('D:\programs\python\Programs\Day8\selenium\chromedriver.exe')
browser.get(url)

school_code = browser.find_element_by_name('treg')
code ='2001'
school_code.send_keys(code)

sleep(2)

click_key = browser.find_element_by_name('bsubmit')

click_key.click()

sleep(5)

html_page = browser.page_source

#//*[@id="Table4"]/tbody/tr[3]/td[7]
#//*[@id="Table4"]/tbody/tr[4]/td[3]

#//*[@id="Table4"]/tbody/tr[3]/td[2]
#//*[@id="Table4"]/tbody/tr[4]/td[2]
A=[]
name=[]
B=[]
C=[]
D=[]
E=[]
for i in range(3,101):
    name.append(browser.find_element_by_xpath('//*[@id="Table4"]/tbody/tr['+str(i)+']/td[2]').text)
    A.append(browser.find_element_by_xpath('//*[@id="Table4"]/tbody/tr['+str(i)+']/td[1]').text)
    B.append(browser.find_element_by_xpath('//*[@id="Table4"]/tbody/tr['+str(i)+']/td[3]').text)
    C.append(browser.find_element_by_xpath('//*[@id="Table4"]/tbody/tr['+str(i)+']/td[5]').text)
    D.append(browser.find_element_by_xpath('//*[@id="Table4"]/tbody/tr['+str(i)+']/td[6]').text)
    E.append(browser.find_element_by_xpath('//*[@id="Table4"]/tbody/tr['+str(i)+']/td[7]').text)
    
    


# Change into csv
    
from pandas import DataFrame 
from collections import OrderedDict
column_name = ['RollNumber','Name','Language','Maths','Physics','Chemistry']

data = OrderedDict(zip(column_name,[A,name,B,C,D,E]))
df = DataFrame(data)
df.to_csv('result.csv')