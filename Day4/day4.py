# -*- coding: utf-8 -*-
"""
Created on Fri May 10 15:41:02 2019

@author: KIIT
"""
from PIL import Image
img = Image.open('face.jpg')
img.width
img.size
img.height

# Coping a file from words.txt to words1.txt
try:
    with open('words.txt','rt') as fp:
        with open('mylist.txt','w') as fp1:
            for row in fp:
                fp1.write(row)
except IOError:
    print("File not found ")
except Exception:
    print("Exception")
finally:
    print('Processed')


with open('mylist.txt','r+') as fp:
    fp.seek(0,2)
    fp.write('\nCompleted List')
    

fp1.closed  # Used to check the status of file

# Creating Absentee file

try:
    with open('Absentee.txt','r+') as fp:
        while True:
            s = input()
            if s==' ':
                print(fp.readlines())
                break
            else:
                fp.write(s+'\n')
except IOError:
    print('File not found')
except Exception:
    print('Exception occurs')
finally:
    print('Processed')
    
import csv
def Read_File(csv_reader):
    '''with open('zoo.csv','r') as csv_file:
        csv_reader= csv.reader(csv_file,delimiter = ',')
        next(csv_reader)'''
    for row in csv_reader:
        print(row)

def Groups(csv_reader):
    l=[]
    '''with open('zoo.csv','r') as csv_file:
        csv_reader= csv.reader(csv_file,delimiter = ',')
        next(csv_reader)'''
    for row in csv_reader:
        if row[0] not in l:
            l.append(row[0])
    print(l)

def Sum():
    s=0
    with open('zoo.csv','r') as csv_file:
        csv_reader= csv.reader(csv_file,delimiter = ',')
        next(csv_reader)
        for row in csv_reader:
            s+=int(row[2])
    print(s)
def Total_Water_needed():
    l=[0]*5
    with open('zoo.csv','r') as csv_file:
        csv_reader= csv.DictReader(csv_file)
        for row in csv_reader:
            if row['animal'] =='elephant':
                l[0]+=int(row['water_need'])
            elif row['animal'] == 'tiger':
                l[1]+=int(row['water_need'])
            elif row['animal'] == 'zebra':
                l[2]+=int(row['water_need'])
            elif row['animal'] == 'lion':
                l[3]+=int(row['water_need'])
            elif row['animal'] == 'kangaroo':
                l[4]+=int(row['water_need'])
                
    
        

try:  
    with open('romeo.txt','r+') as fp:
        l=[]
        for line in fp:
            l.append(line)
            d = {}
        for i in l:
            for j in i.split(' '):
                if j in d:
                    d[j]+=1
                else:
                    d[j] = 1
    print(d)
except IOError:
    print('File not found')
except Exception:
    print('Exception Handler')
finally:
    print('Processed')




# User name
try:  
    print('Enter the file name with proper extension')
    s = input()
    with open(s,'r+') as fp:
        s= fp.readlines()
        print(s[-2],type(s))   
except IOError:
    print('File not found')
except Exception:
    print('Exception Handler')
finally:
    print('Processed') 



# Password

from PIL import Image,ImageFilter
img = Image.open('a.jpg')
img.mode

img_rotate =  img.transpose(Image.ROTATE_270)
img_rotate.show()

img.show()
crop_im = img.crop(box=(160,2,204,10))
crop_im.show()



import hashlib

def hash_file(filename):
   """"This function returns the SHA-1 hash
   of the file passed into it"""

   # make a hash object
   h = hashlib.sha1()

   # open file for reading in binary mode
   with open(filename,'rb') as file:

       # loop till the end of the file
       chunk = 0
       while chunk != b'':
           # read only 1024 bytes at a time
           chunk = file.read(1024)
           h.update(chunk)

   # return the hex representation of digest
   return h.hexdigest()

message = hash_file("[Songs.PK] Agent Vinod - 03 - Raabta.mp3")
print(message)


import os

os.getcwd()