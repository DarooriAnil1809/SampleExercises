#python indentation -spaces at beginning of a code line

if 5 > 2:
    print("Five is greater than 2")

#Indentation error
# if 5 > 2:
# print("five is greater than 2")

if 10 > 2:
    print("Ten Greater than two")
if 10 > 2:
            print("Ten Greater than 2")


#variable declaration
x = 10
y = "HELLO WORLD"
print(x,y)

x = int(10)
y = str("HELLO PYTHON")
z = float(10.52)
print(x,y,z)


#Global Variables

x = "SMART AND"
def myfunc():
    x = "FANTASTIC"
    print("ANIL is " + x)
myfunc()
print("ANIL is" + x)

y = "INTERPRETER"
def myfunct():
    y = "DJANGO"
    print("PYTHON is " + y)
myfunct()
print("PYTHON is " + y)


#Format String
age = 30
txt = "my age is {}"
print(txt.format(age))

#Formatting the string 
quantity = 5
itemno = 56758
price = 200
myorder = "I want {} pieces of item {} for {} dollars"
print(myorder.format(quantity,itemno,price))

tickets = 2
moviename = "GOD Father"
price = 250
objmovie = "I Want {} tickets of {} Movie for {} rupees"
print(objmovie.format(tickets,moviename,price))


#operators
x = 100
x += 5
print(x)

x = 500
x -= 10
print(x)

#list
mylist1 = [1,2,3]
mylist2 = ["C","PYTHON","JAVA"]
print(mylist1,mylist2)

mylist = ["C","PYTHON","JAVA","ML","AI","C#"]
if "D" in mylist:
    print("YES Exist")
else:
    print("NOT EXISTS")


#change list items
mylist = ["C","PYTHON","JAVA","ML","AI","C#"]
mylist[0] = "C Lang"
print(mylist)

#Range of values change
mylist = ["C","PYTHON","JAVA","ML","AI","C#"]
mylist[1:2] = "PYTHON LANG", "JAVA PGM"
print(mylist)

#Add items
#Append() method

mylist = ["C","PYTHON","JAVA","ML","AI","C#"]
mylist.append("SQL")
print(mylist)

mylist = ["C","PYTHON","JAVA","ML","AI","C#"]
mylist.extend(["POSTGRE","SQLLITE"])
print(mylist)


#LOOP LIST
mylist = ["C","PYTHON","JAVA","ML","AI","C#"]
for x in mylist:
    print(x)

mylist = ["C","PYTHON","JAVA","ML","AI","C#","DEVOPS"]
for x in range(len(mylist)):
    print(mylist[x])

#LIST COMPREHENSION
mylist = ["C","PYTHON","JAVA","ML","AI","C#"]
newlist = []
for x in mylist:
    if "A" in x:
        newlist.append(x)
print(newlist)

#LIST COMPREHENSION WRITE IN SINGLE LINE
mylist = ["C","PYTHON","JAVA"]

nayalist = [x for x in mylist if "A"in x]
print(nayalist)


mylist = ["C","PYTHON","JAVA","ML","AI","C#"]
newlist1 = [x for x in mylist if "C#" not in x]
print(newlist1)

#sort function - ascending
mylist = [100,20,52,65,78,25,65,98]
mylist.sort()
print(mylist)

#sort function - decending
mylist = [100,20,52,65,78,25,65,98]
mylist.sort(reverse = True)
print(mylist)


#sort function - alphabetically
mylist = ["C","PYTHON","JAVA","ML","AI","C#"]
mylist.sort()
print(mylist)


#TUPLE

thistuple =("ANIL","SAHASRA","SANVI",30)
print(thistuple)

#Length of tuple
print(len(thistuple))

#one item tuple 
thistuple = ("ANIL",)
print(type(thistuple))

#tuple constructor
thistuple = tuple(("A","N","I","L"))
print(thistuple)

#access tuples
thistuple =("ANIL","SAHASRA","SANVI",30,"VIRAT","Peter Dinklage")
print(thistuple[0])
print(thistuple[5])
print(thistuple[-4])
print(thistuple[:4])
print(thistuple[-4:-1])

thistuple =("ANIL","SAHASRA","SANVI",30,"VIRAT","Peter Dinklage")
if "ANIL" in thistuple:
    print(" exists")
else:
    print("not exists")


#update tuple
thistuple =("ANIL","SAHASRA","SANVI",30,"VIRAT","Peter Dinklage")
y = list(thistuple)
y[0] = "ANIL KUMAR"
thistuple = tuple(y)
print(thistuple)

#add items
thistuple =("ANIL","SAHASRA","SANVI",30,"VIRAT","Peter Dinklage")
y = list(thistuple)
y[3] = "ROHIT SHARMA"
thistuple = tuple(y)
print(thistuple)

thistuple =("ANIL","SAHASRA","SANVI",30,"VIRAT","Peter Dinklage")
y = ("ROHIT SHARMA",)
thistuple += y
print(thistuple)

#LOOP Tuples
thistuple =("ANIL","SAHASRA","SANVI",30,"VIRAT","Peter Dinklage","ROHIT")
for x in thistuple:
    print(x)

#LOOP THROUGH INDEX NUMBERS
thistuple =("ANIL","SAHASRA","SANVI",30,"VIRAT","Peter Dinklage","ROHIT")
for x in range(len(thistuple)):
    print(x)


#While Loop- Tuple
thistuple =("ANIL","SAHASRA","SANVI",30,"VIRAT","Peter Dinklage","ROHIT","PANT")
i = 0
while i < len(thistuple):
    print(thistuple[i])
    i= i+1

#JOIN TUPLES
thistuple =("ANIL","SAHASRA","SANVI",30,"VIRAT","Peter Dinklage","ROHIT")
thistuple1 = ("PANT","DK")
tuple3 = thistuple+thistuple1
print(tuple3)

#DICTIONARIES

mydict = {
    "name": "ANIL",
    "age": 30,
    "Location":"HYD",
}
print(mydict)
print(mydict["name"])
print(mydict['age'])


#Access Dictionary
my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
    }
x = my_dict["Model"]
y = my_dict["Brand"]
print(x)
print(y)

#list of all items - keys

my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
    }
x = my_dict.keys()
print(x)

#Dict - add new item
my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
    }

x = my_dict.keys()
print(x)
x = my_dict["Color"]= "WHITE"
print(x)


#Change the items
my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
    }
my_dict["MANUFACTURE YEAR"] = 2020
print(my_dict)

#if key exists

my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
}
if "Brand" in my_dict:
    print("Exists")
else:
    print("NOT Exists")




#ADD DICTIONARY
my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
}
my_dict["Color"] = "WHITE"
print(my_dict)

#udpate Dictionary
my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
}
# my_dict["Car Type"] = "SEDAN"
# print(my_dict)
my_dict.update({"Car Type" : "Sedan"})
print(my_dict)

#Delete Dictionary
my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
    "Price" : 500000
}
del my_dict["Price"]
print(my_dict)


#Clear Method
my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
}
my_dict.clear()
print(my_dict)

#Complete Dictionary Delete
# my_dict ={
#     "Brand" : "TATA",
#     "Model" : "ALTROZ",
#     "MANUFACTURE YEAR": 2020,
#     "Car Type" : "HATCHBACK",
# }
# del my_dict
# print(my_dict)



#Loop Dictionaries
my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
}
for x in my_dict:
    print(my_dict[x])


#items method to return keys and values
my_dict ={
    "Brand" : "TATA",
    "Model" : "ALTROZ",
    "MANUFACTURE YEAR": 2020,
    "Car Type" : "HATCHBACK",
}
for x in my_dict.items():
    print(x)

#Nested Dictionaries
my_dict ={
    "Brand" : "KIA",
    "Model" : "SELTOS",
    "MANUFACTURE YEAR": 2022,
    "Car Type" : "HATCHBACK",
}

my_nieces = {
    "child1" : {
        "name" : "Candy",
        "year" : 2013

    },
    "child2" : {
        "name" : "Smrithika",
        "year" : 2016
    },

    "child3" : {
        "name" : "Sanvika",
        "year" : 2017
    }
}
print(my_nieces)

#other way create 3 dict then create one dict contain all dict
child1 = {
        "name" : "Candy",
        "year" : 2012

     }
child2 = {
        "name" : "Smrithika",
        "year" : 2015
    }

child3 = {
        "name" : "Sanvika",
        "year" : 2018
    }

myfamily = {
    "child1" : child1,
    "child2" : child2,
    "child3" : child3
}
print(myfamily)

