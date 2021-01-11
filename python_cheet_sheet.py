import json
import requests
import datetime
import pandas as pd
import numpy as np
import time
import csv
import re
import os
import petl
import schedule
# ---------------- data structures ---------------- #
# list

list = [1, 2, 3]
# tupel

tupel = (1, 2, 3)
# set

set = {1, 2, 3}
# dictionery 

dic = {"key1": "value1", "key2": "value2"}

# string


# ---------------- flow control ---------------- #
if condition:
	code
elif condition:
	code
else:
	code
# ----------------
for item in range(start, stop, step):
code

mylist = [x*2 for x in range(0, 11) if x % 2 == 0] // short way for loop & if statement
# ----------------
while boolean_condition:
	code
# ---------------- 
l = list(range(10))
print(l)
l = list(map(lambda x: x*x, l))
print(l)
l = list(filter(lambda x: x > 10 and x < 80, l))
print(l)
# ---------------- functions ---------------- #


def function(*args):
    print(args)


function("eran")
# ----------------

if __name__ == '__main__':
    code

#  ---------------- lambda & map & filter ---------------- #

nums = (1, 2, 3, 4, 5, 6, 7)
result = map(lambda x: x + x + x, nums)
print(list(result))


def square_num(n):
  return n * n


nums = [4, 5, 2, 9]
result = map(square_num, nums)
print(list(result))


def check_even(num): return num % 2 == 0


my_nums = [1, 2, 3, 4, 5, 6]
for item in filter(check_even, my_nums): print(item) -> 2, 4, 6

#  ---------------- files ---------------- #









#  ---------------- object & class ---------------- #






#  ---------------- Regex ---------------- #





#  ---------------- date & time  ---------------- #
import datetime

# current date and time
datetime_object = datetime.datetime.now()
print(datetime_object)

# current date
date_object = datetime.date.today()
print(date_object)
print("Current year:", date_object.year)
print("Current month:", date_object.month)
print("Current day:", date_object.day)

# date class

d = datetime.date(2019, 4, 13)
print(d)

timestamp = date.fromtimestamp(1326244364)
print("Date =", timestamp)

# time class 

# time(hour = 0, minute = 0, second = 0)
a = time()
print("a =", a)

# time(hour, minute and second)
b = time(11, 34, 56)
print("b =", b)
print("hour =", b.hour)
print("minute =", b.minute)
print("second =", b.second)
print("microsecond =", b.microsecond)

# time(hour, minute and second)
c = time(hour = 11, minute = 34, second = 56)
print("c =", c)

# time(hour, minute, second, microsecond)
d = time(11, 34, 56, 234566)
print("d =", d)

# datetime class

a = datetime(2017, 11, 28, 23, 55, 59, 342380)
print("year =", a.year)
print("month =", a.month)
print("hour =", a.hour)
print("minute =", a.minute)
print("timestamp =", a.timestamp())

# timedelta class 

t1 = timedelta(weeks = 2, days = 5, hours = 1, seconds = 33)
t2 = timedelta(days = 4, hours = 11, minutes = 4, seconds = 54)
t3 = t1 - t2

print("t3 =", t3)

# strftime() - datetime object to string

# current date and time
now = datetime.now()

t = now.strftime("%H:%M:%S")
print("time:", t)

s1 = now.strftime("%m/%d/%Y, %H:%M:%S")
# mm/dd/YY H:M:S format
print("s1:", s1)

s2 = now.strftime("%d/%m/%Y, %H:%M:%S")
# dd/mm/YY H:M:S format
print("s2:", s2)

# strptime() - string to datetime object

date_string = "21 June, 2018"
print("date_string =", date_string)

date_object = datetime.strptime(date_string, "%d %B, %Y")
print("date_object =", date_object)


#  ---------------- requests  ---------------- #







#  ---------------- built-in functions  ---------------- #





#  ---------------- collections  ---------------- #

# --- counter --- #
# Counter is a subclass of dictionary object.
# The Counter() function in collections module takes an iterable or a mapping as the argument and returns a Dictionary.
# In this dictionary, a key is an element in the iterable or the mapping and value is the number of times that element exists in the iterable or the mapping.
from collections import Counter

list = [1,2,3,4,1,2,6,7,3,8,1]
cnt = Counter(list)
print(cnt)
# elemnts()
print(list(cnt.elements()))
# most_common()
print(cnt.most_common())
# subtract()
cnt = Counter({1:3,2:4})
deduct = {1:1, 2:2}
cnt.subtract(deduct)
print(cnt)


# --- defaultdict --- #

# --- ordereddict --- #

# --- deque --- #

# --- chainmap --- #

# --- namedtuple --- #





#  ---------------- csv & json  ---------------- #

# --- csv --- #
import csv

# read csv file using csv.reader()
with open('people.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        print(row)

# write csv file using csv.writer()

csv_rowlist = [["SN", "Movie", "Protagonist"], [1, "Lord of the Rings", "Frodo Baggins"],
               [2, "Harry Potter", "Harry Potter"]]
with open('protagonist.csv', 'w') as file:
    writer = csv.writer(file)
    writer.writerows(csv_rowlist)

# read csv file to dictionary with csv.DictReader()

with open("people.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        print(dict(row))

# write csv file from dictionary to file with csv.DictWriter()

with open('players.csv', 'w', newline='') as file:
    fieldnames = ['player_name', 'fide_rating']
    writer = csv.DictWriter(file, fieldnames=fieldnames)

    writer.writeheader()
    writer.writerow({'player_name': 'Magnus Carlsen', 'fide_rating': 2870})
    writer.writerow({'player_name': 'Fabiano Caruana', 'fide_rating': 2822})
    writer.writerow({'player_name': 'Ding Liren', 'fide_rating': 2801})

#  read and write csv with pandas 

pd.read_csv("people.csv")

df = pd.DataFrame([['Jack', 24], ['Rose', 22]], columns = ['Name', 'Age'])
df.to_csv('person.csv')



# --- json --- #
import json

# json to dictionary :

person = '{"name": "Bob", "languages": ["English", "Fench"]}'
person_dict = json.loads(person)
print( person_dict)

# read json file to dictionary

with open('path_to_file/person.json') as f:
  data = json.load(f)

print(data)

# convert dictionary to json :

person_dict = {'name': 'Bob',
'age': 12,
'children': None
}
person_json = json.dumps(person_dict)

print(person_json)

# writing json to a file :

person_dict = {"name": "Bob",
"languages": ["English", "Fench"],
"married": True,
"age": 32
}

with open('person.txt', 'w') as json_file:
  json.dump(person_dict, json_file)


#  ---------------- pandas (dataframes & series) ---------------- #

 Series([3, 6, 9, 12], index=[eran, roni, noa, iris])

data = {"Name": ["Tom", "Jack", "nick", "juli"], "marks": [99, 98, 95, 90]}
   df = pd.DataFrame(data, index=["rank1", "rank2", "rank3", "rank4"])

 df DataFrame(np.arange(25).reshape((5,5)),index=[‘NYC’,’LA’,’SF’,’DC’,’CHI’’],columns=[‘A’,’B’,’C’,’D’,’E’])

df.columns -> give you the columns names
df[age] -> give you the col data
DataFrame(df,columns=[age,name]) - > give you sliced of your dataframe according to the columns you choose.
df.head() -> give the 5 first rows 
df.tail() -> last 5 rows
df.ix[3] -> give row by index you want
df[age] = 35 -> changed the values of all the col
del df[age] -> delete column

# Reindex
# ----------------

ser = Series([1,2,3,4],index = [A,B,C,D]) 
 ser.reindex([A,B,C,D,E,F],fill_value =0)
# Drop entry
# ----------------

ser = Series(np.arange(3),index = [a,b,c])
ser.drop(b) for rows
for col ser.drop(‘age’,axis=1)
# Rank and sort
# ----------------

ser = Series(np.arange(3),index = [c,a,b])
ser.sort_index()
ser.order()
ser.rank()
# Missing data
# ----------------

data = Series([one,two,np.nan,four])
data.isnull()
data.dropna()
data.fillna(1)
# reading and writing text files
# ----------------

            df = pd.read_csv(‘tmp.csv’)
	df.to_csv(‘output.csv’)
# json 
# ----------------

import json 
data = json.loads(json_obj)
df = DataFrame(data)
list1 = [5, 12, 13, 14];
print(json.dumps(list1));
# merge 
# ----------------

dframe1 = DataFrame({'key':['X','Z','Y','Z','X','X'],'data_set_1': np.arange(6)})
dframe2 = DataFrame({'key':['Q','Y','Z'],'data_set_2':[1,2,3]})
pd.merge(dframe1,dframe2)
# concatenate
# ----------------

with series =>
ser1 =  Series([0,1,2],index=['T','U','V'])
	ser2 = Series([3,4],index=['X','Y'])
	pd.concat([ser1,ser2])
with dataframes =>
	dframe1 = DataFrame(np.random.randn(4,3), columns=['X', 'Y', 'Z'])
	dframe2 = DataFrame(np.random.randn(3, 3), columns=['Y', 'Q', 'X'])
	pd.concat([dframe1,dframe2])
# combining 
# ----------------

with series =>
ser1 = Series([2,np.nan,4,np.nan,6,np.nan],
           index=['Q','R','S','T','U','V'])
ser2 = Series(np.arange(len(ser1), dtype=np.float64),
           index=['Q','R','S','T','U','V'])
ser1.combine_first(ser2)
with dataframes =>
dframe_odds = DataFrame({'X': [1., np.nan, 3., np.nan],
                     'Y': [np.nan, 5., np.nan, 7.],
                     'Z': [np.nan, 9., np.nan, 11.]})
dframe_evens = DataFrame({'X': [2., 4., np.nan, 6., 8.],
                     'Y': [np.nan, 10., 12., 14., 16.]})
dframe_odds.combine_first(dframe_evens)
# Grouping and Aggregating
# ----------------


# pivoting
# ----------------

dframe_piv = dframe.pivot('date','variable','value')
# dupliation
# # ----------------
 
            dframe = DataFrame({'key1': ['A'] * 2 + ['B'] * 3, 'key2': [2, 2, 2, 3, 3]})
            dframe.duplicated()
            dframe.drop_duplicates(['key1'])
# mapping 
# ----------------

dframe = DataFrame({'city':['Alma','Brian Head','Fox Park'], 'altitude':[3158,3000,2762]})
state_map={'Alma':'Colorado','Brian Head':'Utah','Fox Park':'Wyoming'}
dframe['state'] = dframe['city'].map(state_map)
# Replace
# ----------------

	ser1 = Series([1,2,3,4,1,2,3,4])
              ser1.replace(1,np.nan)
# regex
# ----------------

import re
text = ‘eran phone number is 054-525-6652’
pattern = ‘phone’
match = re.search(pattern,text) - > return match object
matches = re.findall(pattern,text) - > return list with all the matches
phone = re.search(r’\d{3}-\d{3}-\d{4},text)


#  ---------------- numpy ---------------- #





#  ---------------- spark & pyspark -------------- #

import json
import datetime
import pandas as pd
import numpy as np
import time
import csv
import re
import os
import schedule
import findspark
import pyspark
# import spark
from pyspark import SparkConf
from pyspark import SparkContext
from pyspark.sql import SparkSession
from pyspark.sql import SQLContext
from pyspark.sql.types import ArrayType, StructField, StructType, StringType, IntegerType, DoubleType, DateType
import pyspark.sql.functions as F


def function():
   
   print("eran edri")




if __name__ == '__main__':
    findspark.init()
    sc = SparkContext.getOrCreate()
    sqlContext = SQLContext(sc)
    spark = SparkSession(sc)

    schema = StructType([
        StructField('keyword', StringType(), True),
        StructField('avg_searches_monthly_volume', DoubleType(), True),
        StructField('avg_cpc', DoubleType(), True),
        StructField('dt', StringType(), True)
    ])





#  ---------------- airflow -------------- #

# importing the libaries
from datetime import timedelta
from airflow import DAG
from airflow.operators.python_operator import PythonOperator
from airflow.utils.dates import days_ago

# defining DAG args
default_args = {
    'owner': 'lakshay',
    'depends_on_past': False,
    'start_date': days_ago(2),
    'email': ['airflow@example.com'],
    'email_on_failure': False,
    'email_on_retry': False,
    'retries': 1,
    'retry_delay': timedelta(minutes=5),
    # 'queue': 'bash_queue',
    # 'pool': 'backfill',
    # 'priority_weight': 10,
    # 'end_date': datetime(2016, 1, 1),
    # 'wait_for_downstream': False,
    # 'dag': dag,
    # 'sla': timedelta(hours=2),
    # 'execution_timeout': timedelta(seconds=300),
    # 'on_failure_callback': some_function,
    # 'on_success_callback': some_other_function,
    # 'on_retry_callback': another_function,
    # 'sla_miss_callback': yet_another_function,
    # 'trigger_rule': 'all_success'
}


# define the python function
def my_function(x):
    return x + " is a must have tool for Data Engineers."

# define the DAG
dag = DAG(
    'python_operator_sample',
    default_args=default_args,
    description='How to use the Python Operator?',
    schedule_interval=timedelta(days=1),
)

t1 = PythonOperator(
    task_id='print',
    python_callable= my_function,
    op_kwargs = {"x" : "Apache Airflow"},
    dag=dag,
)

t1




#  ---------------- DB connections ---------------- #

# sqlit - relational DB
import sqlite3

db = sqlite3.connect(':memory:')  # Using an in-memory database
cur = db.cursor()

cur.execute('''CREATE TABLE IF NOT EXISTS Customer (
                id integer PRIMARY KEY,
                firstname varchar(255),
                lastname varchar(255) )''')


cur.execute('''INSERT INTO Customer(firstname, lastname)
               VALUES ('Bob', 'Adams'),
                      ('Amy', 'Smith'),
                      ('Rob', 'Bennet');''')


cur.execute('''SELECT itemid, AVG(price) FROM BoughtItem GROUP BY itemid''')
print(cur.fetchall())

# MongiDB - No relational DB
# pip install pymongo

import pymongo

client = pymongo.MongoClient("mongodb://localhost:27017/")

# Note: This database is not created until it is populated by some data
db = client["example_database"]

customers = db["customers"]
items = db["items"]

customers_data = [{ "firstname": "Bob", "lastname": "Adams" },
                  { "firstname": "Amy", "lastname": "Smith" },
                  { "firstname": "Rob", "lastname": "Bennet" },]
items_data = [{ "title": "USB", "price": 10.2 },
              { "title": "Mouse", "price": 12.23 },
              { "title": "Monitor", "price": 199.99 },]

customers.insert_many(customers_data)
items.insert_many(items_data)



bob = customers.update_many(
        {"firstname": "Bob"},
        {
            "$set": {
                "boughtitems": [
                    {
                        "title": "USB",
                        "price": 10.2,
                        "currency": "EUR",
                        "notes": "Customer wants it delivered via FedEx",
                        "original_item_id": 1
                    }
                ]
            },
        }
    )

customers.create_index([("name", pymongo.DESCENDING)])
items = customers.find().sort("name", pymongo.ASCENDING)

for item in items:
  print(item.get('boughtitems'))  

# SELECT firstname, boughtitems FROM customers WHERE firstname LIKE ('Bob', 'Amy')

for i in customers.find({"$or": [{'firstname':'Bob'}, {'firstname':'Amy'}]}, 
                                 {'firstname':1, 'boughtitems':1, '_id':0}):
     print(i)


# Redis - Cache DB
# $ pip install redis

import redis
from datetime import timedelta

# In a real web application, configuration is obtained from settings or utils
r = redis.Redis()

# Assume this is a getter handling a request
def get_name(request, *args, **kwargs):
    id = request.get('id')
    if id in r:
        return r.get(id)  # Assume that we have an {id: name} store
    else:
        # Get data from the main DB here, assume we already did it
        name = 'Bob'
        # Set the value in the cache database, with an expiration time
        r.setex(id, timedelta(minutes=60), value=name)
        return name

