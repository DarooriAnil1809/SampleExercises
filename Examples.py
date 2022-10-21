import keyword
import math
#Indentation and comments
if 10 > 0:
    #This is comment
    print("Number is positive")
    print("10 is Greater")
else:
    print("Number is Smaller")


# Keywords - To List all keywords in PYTHON
keywords = keyword.kwlist
for key in keywords:
    print(key)


#Built in TYpes
a = 5
print(a)
b = 5.5
print(b)
str = "ANIL KUMAR DAROORI"
print(str)

a, b = (20, 40)
print(a)
print(b)

a, b, c = (10, 25, 30)
print(a, b, c)

# Extended Sequence * Multiple Elements
p, *q = "Hello"
print(p)
print(*q)

# AuGmented AssiGment
a = 5
a += 1
print(a)
a = 5
a = a+5
print(a)

# Input and Output Functions
# MULTI LINE COMMENTS
"""
name = input("Enter your Name")
print("Hello," + name)
print(type(name))

num = int(input("Enter a number"))
add = num + 1
print(add)

a, b, c = map(int, input("Enter the numbers: ").split())
print(" The Numbers are", end=" ")
print(a, b, c)
"""
# MULTILINE COMMENTS
# Seperator
print("HELLO", "WELCOME", "TO", "PYTHON PROGRAMMING", sep=("\n"))
print("HELLO", "WELCOME", "TO", "PYTHON PROGRAMMING", sep=("-"))

# END ATTRIBUTE KEYWORD - 2 Print Statements in sin
print("HELLO", end=" ")
print("WELCOME TO INDIA")


#Operators
#Arithmetic Operations EXAMPLE
a = 10
b = 20
add = a+b
sub = a-b
mul = a*b
div = a/b
moddiv = a%b
floordiv = a//b
exp = a**b
print("Addition of Two Numbers",add)
print("Subtraction of Two Numbers",sub)
print("Multiplication of Two Numbers",mul)
print("Division of Two Numbers",div)
print("Module Division of Two Numbers",moddiv)
print("Floor Division of Two Numbers",floordiv)
print("Exponent of Two Numbers",exp)


#Relation Operators - Condition Check

a = 10
b = 20
print("The Value of A Greater than B is",a>b)
print("The Value of A Less than B is",a<b)
print("The Value of A is equal to B is",a==b)
print("The Value of A is not equal to B is",a!=b)
print("The Value of A is Greater than equal to B is",a>=b)
print("The Value of A less than equal to B is",a<=b)

#Bitwise Operators 
#LOGICAL OPERATORS
#Membership Operators and Identity Operators
#IN OPERATOR
list1 = [1,2,3,4,5]
list2 = [6,7,8,9]
for item in list1:
    if item in list2:
        print("OverlappinG")
        break
else:
        print("not overlappinG")


list1 = ["ANIL", "KUMAR", "DAROORI"]
list2 = ["AGRA", "HYDERABAD", "NOIDA"]
for name in list1:
    if name in list2:
        print("OVERLAPPED")
        break
else:
        print("NOT OVERLAPPED")

#NOT IN OPERATOR
a = 20
b = 30
list1 = [10,20,30,40,50]
if(a not in list1):
    print(" A not present in list")
else:
    print("A present in list")

if(b not in list1):
    print("B not present in list")
else:
    print("B present in list")



#Idetity Operators
a = 10
b = 10
print(a is b)
id(a)
id(b)



#Control Structures
#Conditional Statements
#if Statement

i = 100
if(i > 200):
    print("i Value is Greater than 200")
else:
    print("i value is less than 200 ")

#Nested If Statement
i = 1000
if(i == 1000):
    if(i<150):
        print("i is smaller than 150")
    if(i<120):
        print("i is smaller than 120")
    else:
        print("i is Greater than 150")



#if..elif..else

i = 20
if( i==10):
    print("i is 10")
elif(i == 15):
    print(i is 15)
elif(i == 18):
    print(i is 18)
elif(i == 20):
    print("i is 20")

else:
    print("is is not present")


#While Loop

i = 0
while (i<100):
    i = i+1
    print(i)

#While Loop - SINGLE LINE
count = 0
while(count<25): count += 1; print(count)

#Print all letters except K and U

i = 0
a ="ANIL KUMAR DAROORI"
while i < len(a):
    if a[i] == 'K' or a[i] == 'U':
        i += 1
        continue

    print('Current Letter:', a[i])
    i+=1




#Math and Random Modules
#import math module
#CeilinG Module
a = math.ceil(10.3)
print(a)


a = 10
b =20
x = math.copysign(a,b)
print(x)

