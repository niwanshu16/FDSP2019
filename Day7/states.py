# -*- coding: utf-8 -*-
"""
Created on Wed May 15 11:27:31 2019

@author: KIIT
"""
# DISTRICTS of a state in india 
import json
with open('states.json') as fp:
    data = json.load(fp)


# Print the districts of any state
s = input()
district = data['states'][1]
for i in data['states']:
    if i['state']==s:
        print(i['districts'])
        print('Total District {}'.format(len(i['districts'])))
        break
    
# Now we have to alter all the state name 
        
for i in data['states']:
    i['state']=i['state'].lower()


# dumb data into a json file
    
with open('new_states.json','w') as fp:
    json.dump(data,fp,indent=2)
    


from urllib.request import urlopen

with urlopen("https://finance.yahoo.com/webservice/v1/symbols/allcurencies/quote?format=json") as response:
    source = response.read()
  