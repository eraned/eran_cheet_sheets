import numpy as np 
import pandas as pd
import json
import re
# ----------------
list = [1,2,3]
tupel = (1,2,3)
set = {1,2,3}
dic = {"key1" : "value1","key2":"value2"}
# ----------------
if condition :
	code
elif condition :
	code
else:
	code
# ----------------
for item in range(start,stop,step):
code

mylist = [x*2 for x in range(0,11) if x%2==0] // short way for loop & if statement
# ----------------
while boolean_condition:
	code
# ----------------
l = list(range(10))
print(l)
l = list(map(lambda x:x*x, l))
print(l)
l = list(filter(lambda x: x > 10 and x < 80, l))
print(l)
# ----------------
def function (*args):
    print(args)

function("eran")
# ----------------

if __name__ == '__main__':
    code