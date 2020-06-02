### -------------------------------- ###
### 2.4.1 simple imports
### -------------------------------- ###

import time
print("hello")
time.sleep(1)
print("world!")
print(time.time())





### -------------------------------- ###
### 2.4.2 more complex imports
### -------------------------------- ###

from datetime import date

today = date.today()
print(today)

day_of_the_week = date.weekday(today)
print(day_of_the_week)
