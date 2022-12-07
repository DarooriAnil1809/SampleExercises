# CreatinG List
from audioop import avg
from math import factorial
from random import Random, random


list = []
type(list)
list1 = [10, 20, 30]
list2 = [10, 20.50, "ANIL"]
print(list1)
print(list2)

# AccessinG List

list1 = [100, 200, 300, 500, 600]
print(list1[0])
print(list1[1])
print(list1[-1])

# update or reassiGn list

list1 = [100, 200, 300, 500, 600]
list1[0] = 1000
print(list1)

# slicinG
list = [10, 20, 30, 40, 50, 60]
print(list[0:2])
print(list[0:4])
print(list[:])

# Multi-Dimesional List
list = [10, 20, 30]
list1 = [[10, 20, 30], [50, 70, 90]]
print(list1)
print(list1[0])
print(list1[0][0])
print(list1[1][2])
print(list1[1][1])

# List Basic Operations

# ADD LIST - CONCATENATE LIST
list = [111, 123, 132]
list1 = [1111, 1234, 3214]
list2 = [1010, 4120, 5240]
listresult = list+list1+list2
print(listresult)

# Star Repetition
list = [10, 20, 30]
result = 4*list
print(result)

# list to list multiple not allows
"""
list = [1,2,3]
list1 = [2,3,4]
result = list*list1
print(result)
"""

# lenGth of List
list = [10, 20, 30, 40, 50, 60, 70, 80]
a = len(list)
print(a)
list1 = [1, 2, 3, 4, 54, 8, 89, 7, 5, 4, 5445]
b = len(list)
print(b)

# Min and Max list
list = [10, 20, 30, 40]
a = min(list)
b = max(list)
c = sum(list)
print(a)
print(b)

# Membership List
#Build in Functions - Append, Extend, Insert
list = [10, 20, 30]
list.append(60)
print(list)

list = [10, 20, 30, 40]
list.extend([201, 202, 203, 204])
print(list)

list = [100, 102, 103, 104]
list.insert(4, 105)
list.insert(1, 1000)
print(list)

# Remove Function
list = [100, 200, 201, 202, 301]
list.remove(100)
print(list)

# Pop function - last element delete
list = [1, 2, 3, 4, 5, 6]
list.pop()
print(list)


list = [1, 2, 3, 4, 5, 6]
del list[0]
print(list)

# Sort function
list = [50, 20, 30, 48, 65, 78, 98, 58]
list.sort()
print(list)

# reverse order of list - decendinG order
list = [50, 45, 78, 25, 65, 32, 12, 45, 78]
list.sort(reverse=True)
print(list)

# Reverse of list
list = [62, 45, 89, 74, 85, 12, 32, 24, 26, 89]
list.reverse()
print(list)


# LIST COMPREHENSION - [expression, iterations, condition]

list = [ele for ele in range(10)]
print(list)

list = [ele*ele for ele in range(15)]
print(list)

# to print even numbers in list
list = [ele*ele for ele in range(15) if ele % 2 == 0]
print(list)

# cubes
list = [ele**2 for ele in range(15) if ele % 2 == 0]
print(list)

list = [list for list in range(100) if list % 2 == 0]
print(list)


list = [ele for ele in range(500)]
print(list)


# a = []
# for x in range(100):
#     num = Random.randint(1,501)
#     a.append(num)
# print(a)

# a = [random.randint(1, 501) for x in range(100)]
# print(a)
# print(len(a))



#Sum of all list items

List = [list for list in range(50)]
i = 0
for i in list:
    i = i+1
    print(i)