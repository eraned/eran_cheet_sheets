import numpy as np
import pandas as pd
import json
import re
# ----------------
list = [1, 2, 3]
tupel = (1, 2, 3)
set = {1, 2, 3}
dic = {"key1": "value1", "key2": "value2"}
# ----------------
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
# ----------------


def function(*args):
    print(args)


function("eran")
# ----------------

if __name__ == '__main__':
    code

# lambda & map & filter
# ----------------

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

#  dataframes & series
# ----------------

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



