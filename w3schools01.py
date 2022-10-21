#LOOPS

#PYTHON If...Else

#if...
a =300
b =200
if a > b:
    print("A is Greater than b")
else:
    print("B is Greater than A")

#if...elif....
a = 200
b = 200
if a > b:
    print("A is greater than B")
elif a == b:
    print(" A is equal to B")
else:
    print("B is greater than A")


#short hand if
a = 250
b = 50
c = 20
if a > b: print("A is greater than B")

#short hand if..else..
x = 202
y = 500
print("x greater than y") if x > y else print(" y is greater than x")


#Nested If....
x = 41
if x > 10:
    print("Above 10")
    if x >20:
        print("Above 20")
    else:
        print("but not above 10")
 
#while loop
i = 1
while i <= 6:
    print(i)
    i = i + 1

#Break Statement

i = 1
while i < 6:
    print(i)
    if i == 3:
        break
    i += 1

#continue statement
i = 0
while i < 6:
    i = i + 1
    if i == 3:
        continue
    print(i)

#else statement

i = 1
while i < 6:
    print(i)
    i += 1
else:
    print("No Longer less than 6")


#For Loops

friends = ["ANIL","VIRAT","PD","KALPIKA","VINDHYA","CHARISHMA"]
for x in friends:
    print(x)

#Loop Through String
for x in "ANIL":
    print(x)

#Break Statement
friends = ["ANIL","VIRAT","PD","KALPIKA","VINDHYA","CHARISHMA"]
for x in friends:
    print(x)
    if x == "VINDHYA":
        break
    print(x)


#Continue Statement
friends = ["ANIL","VIRAT","PD","KALPIKA","VINDHYA","CHARISHMA"]
for x in friends:
    if x == "PD":
        continue
    print(x)

#Range Function
friends = ["ANIL","VIRAT","PD","KALPIKA","VINDHYA","CHARISHMA"]
for x in range(2):
    print(x)

friends = ["ANIL","VIRAT","PD","KALPIKA","VINDHYA","CHARISHMA"]
for x in range(4,6):
    print(x)


#NESTED LOOPS

friends = ["ANIL","VIRAT","PD","KALPIKA","VINDHYA","CHARISHMA"]
location= ["HYD","DELHI","US","HYD","HYD","AP"]
for x in friends:
    for y in location:
        print(x,y)

#pass statement
#loops cannot be empty, loop no content use pass statement
friends = ["ANIL","VIRAT","PD","KALPIKA","VINDHYA","CHARISHMA"]
for x in [0,2,7]:
    pass


#python Functions - block of code
#creating the function
def my_function():
    print('HELLO 1st FUNCTION')
my_function()

#Function Example - single argument/parameter

def my_functionwithparameter(fname):
    print(fname + " "+ "Mr"+ "")
my_functionwithparameter("Anil")
my_functionwithparameter("Virat")
my_functionwithparameter("Rohit")

#Mutliple Argements
def my_func(fname,lname,age):
    print(fname,lname,age)
my_func("ANIL","Kumar", 30)
my_func("Virat","Kohli", 32)

#Arbitrary Argements *args

def my_function(*names):
    print("employee names" + names[2])
my_function("ANIL","Kumar","ROHIT")



#Keyword Arguments

def my_functionkeyword(child3, child2, child1):
    print("youngest Child is" + child3)
my_functionkeyword(child1 ="ANIL", child2 = "Ravi Teja", child3 = "kanna")



#Arbitrary Keyword Argements *kwargs
def my_funct(**employees):
    print("Total Employees" , " " + employees["names"])
my_funct(names = "ANIL")
my_funct(names = "PK")
my_funct(names = "Sk")
my_funct(names = "RK")


#Default Parameter Value
def my_functionDefaultvalue(country ="INDIA"):
    print("I am from", " " + country)
my_functionDefaultvalue("Austria")
my_functionDefaultvalue("RUSSIA")
my_functionDefaultvalue()


#Passing List as Argument

def my_functionlist(food):
    for x in food:
        print(x)
fruits = ['APPLE','BANANA','SAPOTA']
my_functionlist(fruits)


#Return Values

def my_functionreturnvalues(x):
    return 5*x
print(my_functionreturnvalues(5))
print(my_functionreturnvalues(15))

def my_functionadd(x):
    return 100+x
print(my_functionadd(200))

def my_functionexp(x):
    return x
print(my_functionexp(2))



#Recursion - function call itself

def my_functionRecursion(k):
    if(k > 0):
        result = k + my_functionRecursion(k - 1)
        print(result)
    else:
        result = 0
    return result
        
print("Recursion Result Example")
my_functionRecursion(6)




#Lambda Function
#Anonymous function - many arguments but 1 expression

#Example - add 10 to argument a
x = lambda a : a + 10
print("Simple Lambda Example")
print(x(5))


x = lambda a, b : a*b
print("Lambda Example")
print(x(5,6))

x = lambda a,b,c : a+b+c
print("Lambda function example")
print(x(3,9,78))


def my_lambdaFunction(n):
    return lambda a : a * n
mydoubler = my_lambdaFunction(2)
print(mydoubler(11))

def my_lambda(n):
    return lambda a : a * n
myfunct = my_lambda(10)
print(myfunct(20))



def my_functionlambda(n):
    return lambda a : a * n
doublefunct = my_functionlambda(2)
triplefunct = my_functionlambda(3)

print(doublefunct(10))
print(triplefunct(20))



#ARRAYS 
#create the array
cars = ["FORD","BMW","TATA"]

#accessing the array using index
x = cars[0]
print(x)

#Modify the array
cars = ["FORD","BMW","TATA"]
cars[0] = "BMW"
cars[1] = "FORD"
print(cars)

#Length of array
cars = ["FORD","BMW","TATA"]
x = len(cars)
print(x)

#Looping array elements
cars = ["FORD","BMW","TATA","TOYOTA"]
for x in cars:
    print(x)


#adding elements
cars = ["FORD","BMW","TATA"]
cars.append("HONDA")
print(cars)


