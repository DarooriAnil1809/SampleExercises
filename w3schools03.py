import json
import re

#JSON - JAVASCRIPT OBJECT NOTATION
# STORING and EXCHANGING DATA
#BUILT-IN PACKAGE JSON
#import json

#JSON DATA to PYTHON
#json data
x ='{"name" : "ANIL", "age": 30, "City": "HYD"}'
print(x)

#parse x
y = json.loads(x)
print(y)

print(y['age'])


#CONVERTS PYTHON TO JSON
#python object DICT
x = {
  "name": "John",
  "age": 30,
  "city": "New York"
}

#Converts to JSON
y = json.dumps(x)

print(y)


#ExAMPLE

import json

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}

print(json.dumps(x, indent=4, sort_keys=True))








#PYTHON REGEx - Regular Expression, sequence of characters that forms search pattern
#import re

#Example

#Check if the string starts with "The" and ends with "Spain":

txt = "The rain in Spain"
x = re.search("^The.*Spain$", txt)

if x:
  print("YES! We have a match!")
else:
  print("No match")



  #PYTHON PIP
  #PACKAGE MANAGER for PYTHON PACKAGES or Modules

  #PIP VERSION
    #pip --version

    #pip list
    #pip freeze




#Exception Handing
# Try...except....else....finally

# try:
#     print(x)
# except:
#     print("exception occured")
# else:
#     print("Exception")
# finally:
#     print("Finally block")


# username = input("Enter username")
# print("username is", " " + username)


#string formatting
price = 100
txt = "The price is {} dollars"
print(txt.format(price))

age = 36
name = "John"
txt = "His name is {1}. {1} is {0} years old."
print(txt.format(age, name))


