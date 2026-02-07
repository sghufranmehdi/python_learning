import math
math.sqrt(15)
math.pi

from math import sqrt, pi
sqrt(15)
print(pi)

import random as rnd
number = rnd.randint(1, 100)
print(number)

choices = ['apple', 'banana', 'cherry']
fruit = rnd.choice(choices)
print(fruit)

import datetime as dt
now = dt.datetime.now()
print(now)

import os
current_directory = os.getcwd()
print(current_directory)

import json
data = {'name': 'Alice', 'age': 30, 'city': 'NYC'}
json_string = json.dumps(data)
print(json_string)