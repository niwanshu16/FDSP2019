# -*- coding: utf-8 -*-
"""
Created on Tue May 14 13:11:40 2019

@author: KIIT
"""
import json   
json_string = """
{
    "researcher": {
        "name": "Ford Prefect",
        "species": "Betelgeusian",
        "relatives": [
            {
                "name": "Zaphod Beeblebrox",
                "species": "Betelgeusian"
            }
        ]
    }
}"""
data = json.loads(json_string)  
for i in data:
    del data[i]['species']
    
    
    
'''
.load is used to load data from file
.loads is used to load data from string
'''
new_string = json.dump(data)


# Create a valid json object

Object = """[{
		"student": {
			"name": "Niwanshu Maheshwari",
			"Phone Number": 9898393434,
			"Address": "Jaipur"
		}
	},
	{
		"Faculty": [{
				"name": {
					"fname": "Surendra",
					"lname": "Bajaj"
				},
				"Photo": "url",
				"Department": "CSE",
				"Research": ["ML", "DL", "AI"],
				"Contact Details ": {
					"mobile number": [3298484329, 897234878],
					"emailid": ["sjdalhdq", "jfhqkjfhl"]
				}
			},
			{
				"name": {
					"fname": "Surendra",
					"lname": "Bajaj"
				},
				"Photo": "url",
				"Department": "CSE",
				"Research": ["ML", "DL", "AI"],
				"Contact Details ": {
					"mobile number": [3298484329, 897234878],
					"emailid": ["sjdalhdq", "jfhqkjfhl"]
				}
			}
		]
	}
]
"""

data = json.loads(Object)

for i in data:
    print(i["student"]["name"])
    break

import requests
s = input()
url1 = 'http://api.openweathermap.org/data/2.5/weather?'
url2='q='
url3 = '&appid=e9185b28e9969fb7a300801eb026de9c'

url =url1+url2+s+url3

info = requests.get(url)
storage = info.json()
lon_lat= storage["coord"]
weather_cond = storage["weather"]
wind_speed =storage['wind']
sunrise = storage['sys']['sunrise']
sunset = storage['sys']['sunset']
sunrise =str( str(list1[3])+':'+str(list1[4])+':'+str(list1[5]))
sunset = str( str(list2[3])+':'+str(list2[4])+':'+str(list2[5]))
Dict1 = {"Longitude_Latitude":lon_lat,"WeatherConditions":weather_cond,
         "WindSpeed":wind_speed,"Sunrise" : sunrise,"Sunset" : sunset}



#http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
#Check with http://api.fixer.io/latest?base=USD&symbol=EUR

#8221536910c584b29486
url1 = 'http://data.fixer.io/api/latest?access_key=006205c4dc6c53e8b3435b546da49d16'
data = requests.get(url1)
info = data.json()
type(info)
info['rates']['INR']