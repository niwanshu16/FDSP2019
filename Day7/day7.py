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
import time
def convert_timestamp(time1):
    list1=list(time.localtime(time1))
    return str(list1[3])+':'+str(list1[4])+':'+str(list1[5])

def convert_temp(temp):
    x = temp-273.15
    return x
    
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
temp,temp_max,temp_min = storage['main']['temp'],storage['main']['temp_max'],storage['main']['temp_min']
temp = convert_temp(temp)
temp_max = convert_temp(temp_max)
temp_min= convert_temp(temp_min)
sunrise = convert_timestamp(sunrise)
sunset =  convert_timestamp(sunset)
Dict1 = {"Longitude_Latitude":lon_lat,"WeatherConditions":weather_cond,
         "WindSpeed":wind_speed,"Sunrise" : sunrise,"Sunset" : sunset,
         "Temperature":{"Temp":temp,"Temp_max":temp_max,"Temp_min":temp_min}}
                                                                                     
print(Dict1)


#http://free.currencyconverterapi.com/api/v5/convert?q=USD_INR&compact=y
#Check with http://api.fixer.io/latest?base=USD&symbol=EUR

#8221536910c584b29486
url1 = 'http://data.fixer.io/api/latest?access_key=006205c4dc6c53e8b3435b546da49d16'
data = requests.get(url1)
info = data.json()
type(info)
info['rates']['INR']




url1="https://www.google.com/maps/embed/v1/place?"
url2="q=place_id:ChIJgeJXTN9KbDkRCS7yDDrG4Qw&key=AIzaSyBVXH7cAtN7PyM-_xE35j3SCdsEEv8CWWk"
url = url1 + url2
data = requests.get(url)
store_data = data.json()
r = data.text 

import urllib.request
import json
import requests
url1 = 'https://www.google.com/maps/embed/v1/place?'
url2='key=AIzaSyBVXH7cAtN7PyM-_xE35j3SCdsEEv8CWWk'
url3='&q=Eiffel+tower,Paris+France'

url = url1+url2+url3
"""
uh = urllib.request.urlopen(url)
data = uh.read()
js = json.loads(data.decode("utf-8"))
"""
data = requests.get(url)
store_data = data.content







#____________________________________________

r = requests.get('https://imgs.xkcd.com/comics/python.png')
with open('comic1.png','wb') as fp:
    fp.write(r.content)


