
import sys
import datetime

# 01 Bubble Sort Example


def bubblesort(elements):
    swapped = False
    # Looping the size of array from last index[-1] to index[0]
    for n in range(len(elements)-1, 0, -1):
        for i in range(n):
            if elements[i] > elements[i+1]:
                swapped = True
                # swapping data if elements less than next element in array
                elements[i], elements[i+1] = elements[i+1], elements[i]
        if not swapped:
            return


elements = [28, 30, 14, 78, 95, 65, 75, 23, 31, 42, 51]
print("unsorted list,")
print(elements)
bubblesort(elements)
print("sorted array")
print(elements)


# python version
print('PYTHON VERSION')
print(sys.version)
print("Version Info")
print(sys.version_info)

# python --version - command line command

# Current Date and Time

displaydate = datetime.datetime.now()
print("Current Date and Time")
print(displaydate.strftime("%Y-%m-%d %H:%M:%S"))
