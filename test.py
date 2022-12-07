list = [list for list in range(100) if list % 2 == 0]
print(list)


# #normal function
# def cube(y):
#     return y*y*y
# print(cube(3))

# lambda function

# def cube(x):
#     return x*x*x
def lambdacube(x): return x*x*x


print("lambda function result", lambdacube(5))


List = [list for list in range(50)]
i = 0
for i in list:
    i = i+1
    print("sum of list: ", i )
