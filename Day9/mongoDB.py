# -*- coding: utf-8 -*-
"""
Created on Thu May 16 16:02:56 2019

@author: KIIT
"""

import pymongo

client = pymongo.MongoClient("mongodb://niwanshu:niwanshu29@cluster-shard-00-00-ouyxk.mongodb.net:27017,cluster-shard-00-01-ouyxk.mongodb.net:27017,cluster-shard-00-02-ouyxk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster-shard-0&authSource=admin&retryWrites=true")
db = client.db_university
db.Student.drop()

def add_data(name,age,roll_no,branch):
    unique_stud = db.Student.find_one({"roll_number":roll_no})
    if unique_stud:
        return "Student Exist"
    db.Student.insert_one({
            "Name":name,
            "Age":age,
            "roll_number":roll_no,
            "Branch":branch
            })
    return "Added Successfully"


add_data("Niwanshu",20,51,'CSE')
add_data("Rahul",20,52,'CSE')
add_data("Nitesh",20,53,'CSE')
add_data("Pankaj",20,54,'CSE')
add_data("Adarsh",20,55,'CSE')
add_data("Neeraj",20,56,'CSE')
add_data("Kishore",20,57,'CSE')
add_data("Ayush",20,58,'CSE')
add_data("Ankit",20,59,'CSE')
add_data("Rupam",20,60,'CSE')





# 3rd question
client = pymongo.MongoClient("mongodb://niwanshu:niwanshu29@cluster-shard-00-00-ouyxk.mongodb.net:27017,cluster-shard-00-01-ouyxk.mongodb.net:27017,cluster-shard-00-02-ouyxk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster-shard-0&authSource=admin&retryWrites=true")
db = client.BidData


def add_data(bidid,item,deptname,qty,startdate,enddate):
    db.Bidding.insert_one({
            "BidID":bidid,
            "Item(s)":item,
            "DepartmentName":deptname,
            "Quantity":qty,
            "StartDate":startdate,
            "EndDate":enddate
            })
    return "Added Successfully"

for i in range(len(A)):
    add_data(A[i],B[i],C[i],D[i],E[i],F[i])
    





# Question 4  , ODI team ranking 
    
client = pymongo.MongoClient("mongodb://niwanshu:niwanshu29@cluster-shard-00-00-ouyxk.mongodb.net:27017,cluster-shard-00-01-ouyxk.mongodb.net:27017,cluster-shard-00-02-ouyxk.mongodb.net:27017/test?ssl=true&replicaSet=Cluster-shard-0&authSource=admin&retryWrites=true")
db = client.oditeam

import csv
with open('rating_odi.csv') as fp:
    csv_reader = csv.reader(fp,delimiter =',')
    next(csv_reader)
    l=[]
    for row in csv_reader:
        l.append(row)


def add_data(name,wmatch,rating,rpoints):
    db.oditeam_rank.insert_one({
            "CountryName":name,
            "WeightedMatch":wmatch,
            "Rating":rating,
            "RatingPoints":rpoints
            })
    return "Added Successfully"
for i in l:
    add_data(i[1],i[2],i[3],i[4])




