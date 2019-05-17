# -*- coding: utf-8 -*-
"""
Created on Wed May 15 16:09:58 2019

@author: KIIT
"""

from bs4 import BeautifulSoup
import requests

with open('simple.html') as fp:
    soup = BeautifulSoup(fp,"lxml")

print(soup.prettify())

print(soup.title)
print(soup.title.text)

match = soup.find('div')
print(match.h1)
print(match.h1.text)

match = soup.find('div',class_='header')

for article in soup.find_all('div'):
    headline  =  article.p.text
    print(headline)
    
    
# Scrapping a real data
    
wiki = "https://en.wikipedia.org/wiki/List_of_state_and_union_territory_capitals_in_India"
source = requests.get(wiki).text
soup = BeautifulSoup(source,"lxml")

all_tables = soup.find_all('table')

print(all_tables)

right_table = soup.find('table',class_='wikitable')

A=[]
B=[]
C=[]
D=[]
E=[]
F=[]

for rows in right_table.findAll('tr'):
    cells = row.findAll('td')
    states = row.findAll('th')
    if len(cells)==6:
        A.append(states[0].text.strip())
        B.append(cells[1].text.strip())
        C.append(cells[2].text.strip())
        D.append(cells[3].text.strip())
        E.append(cells[4].text.strip())
        F.append(cells[5].text.strip())
        
        
        

