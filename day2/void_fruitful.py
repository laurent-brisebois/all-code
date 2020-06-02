### -------------------------------- ###
### 2.5.1 void function
### -------------------------------- ###

def hello(name, age):
    age_in_days = age*365
    print("hello and goodbye")


x = hello("Laurent", 105)
print(x)
type(x)

### -------------------------------- ###
### 2.5.1 fruitful functions
### -------------------------------- ###

def age_in_days(age):
    age_in_days = age*365
    return age_in_days

y = age_in_days(33)
print(y)
type(y)
