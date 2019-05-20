# -*- coding: utf-8 -*-
"""
Created on Mon May 20 18:00:13 2019

@author: KIIT
"""

from selenium import webdriver
import matplotlib.pyplot as plt

url = 'https://en.wikipedia.org/wiki/List_of_states_and_union_territories_of_India_by_area'
browser = webdriver.Chrome('D:\programs\python\Programs\Day8\selenium\chromedriver.exe')
browser.get(url)

#//*[@id="mw-content-text"]/div/table[2]/tbody/tr[1]/td[5]
#//*[@id="mw-content-text"]/div/table[2]/tbody/tr[2]/td[3]

#//*[@id="mw-content-text"]/div/table[2]/tbody/tr[29]/td[1]

#//*[@id="mw-content-text"]/div/table[2]/tbody/tr[30]/td[1]
#//*[@id="mw-content-text"]/div/table[2]/tbody/tr[36]/td[1]
def fx(i):
    return int(float(i))
A=[]
B=[]
for i in range(1,7):
    element = browser.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[2]/a').text
    A.append(element)
    element = browser.find_element_by_xpath('//*[@id="mw-content-text"]/div/table[2]/tbody/tr['+str(i)+']/td[5]').text
    B.append(element)

B = list(map(fx,B))
explode = [0]*6
explode[0] = 0.35
plt.pie(B,labels=A,explode = explode,autopct='%1.2f%%')
plt.show()
plt.savefig('top6_area.jpg')