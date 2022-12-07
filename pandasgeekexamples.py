import pandas as pd
import numpy as np


# Creating Series - PANDAS

# Creating Empty Series
ser = pd.Series()
print(ser)
# Simple Array
data = np.array(['A', 'N', 'I', 'L'])
ser = pd.Series(data)
print("The Series")
print(ser)


# Creating DataFrame
# Calling DataFrame Constructor
df = pd.DataFrame()
print(df)


# List of Strings
list = ['PANDAS', 'ARE', 'USED', 'TO', 'ANALYZE', 'DATA']

# Calling DataFrame COnstuctor on LIst
df = pd.DataFrame(list)
print("DATAFRAME")
print(df)


# Create DataFrame using Dictionaries
dict = {'Name': ['ANIL', 'ROHIT', 'CHARISHMA', 'POOJA'],
        'Age': [30, 25, 26, 20]

        }
df = pd.DataFrame(dict)
print(df)


# DataFrame Example
dict = {'Name': ['Hales', 'Buttler', 'Stokes', 'Salt'],
        'Age': [30, 31, 32, 30],
        'Address': ['UK', 'London', 'Manchester', 'Edenburgh'],
        'Qualification': ['BTECH', 'MCA', 'MBA', 'BCOM']

        }
# convert dict to Dataframe
df = pd.DataFrame(dict)
print(df)

# Two Columns
print(df[['Name', 'Qualification']])


# BASIC OPERATIONS
# COLUMN ADDITION - Several Ways

# Define Dictionary Data contains Employee Data
employeedata = {'Employee Name': ["Daroori", "Anil", "Dr.Bhavika", "Dr.Samanth"],
                'Designation': ["SE", "Data Analyst", "Surgeon", "Anesthesia"],
                'Location': ["Hyderabad", "Uppal", "Gujarat", "Hyd"],
                'Age': [30, 30, 30, 32]

                }

# convert dictionary to dataframe
df = pd.DataFrame(employeedata)

# Declare the list that should be added to employee data
EmployeeID = ['CBHY01', '07Dn1A', 'MB0254', 'SR1251']

# using EmployeeID as Column name
# Equated it to the list
df['EmployeeID'] = EmployeeID
print(df)


# METHOD 2
# By Using DataFrame.insert()
# Freedom to add column any position


# Define Dictionary Data contains Employee Data
employeedata = {'Employee Name': ["Daroori", "Anil", "Dr.Bhavika", "Dr.Samanth"],
                'Designation': ["SE", "Data Analyst", "Surgeon", "Anesthesia"],
                'Location': ["Hyderabad", "Uppal", "Gujarat", "Hyd"],
                'Age': [30, 30, 30, 32]

                }

# convert dictionary to dataframe
df = pd.DataFrame(employeedata)

# using dataframe.insert() to add column
df.insert(0, "EmployeeID", ['DR01', 'AN01', 'BH01', 'SM01'], True)
print("INSERT COLUMN - ANY POSITION")
print(df)


# METHOD 3
# By Using DataFrame.Assign()
employeedata = {'Employee Name': ["Daroori", "Anil", "Dr.Bhavika", "Dr.Samanth"],
                'Designation': ["SE", "Data Analyst", "Surgeon", "Anesthesia"],
                'Location': ["Hyderabad", "Uppal", "Gujarat", "Hyd"],
                'Age': [31, 30, 32, 32]

                }
df = pd.DataFrame(employeedata)
df2 = df.assign(EmployeeID=['DR01', 'AN01', 'BH01', 'SM01'])
print(df2)


# METHOD 4
# By Using Dictionary
employeedata = {'Employee Name': ["Daroori", "Anil", "Dr.Bhavika", "Dr.Samanth"],
                'Designation': ["SE", "Data Analyst", "Surgeon", "Anesthesia"],
                'Location': ["Hyderabad", "Uppal", "Gujarat", "Hyd"],
                'Age': [31, 30, 32, 32]

                }
EmployeeID = {'Daroori': "CBHY01", 'Anil': "07Dn1A",
              'Dr.Bhavika': "MB0254", 'Dr.Samanth': "SR1251"}

df = pd.DataFrame(employeedata)
df['EmployeeID'] = EmployeeID
print("Dictionary Method")
print(df)


# ROW ADDITION
# METHOD 1 - Concat Old DataFrame with New One
df = pd.read_csv(r'D:\Filehandling\nba.csv', encoding='latin1')
df.head(10)
new_row = pd.DataFrame({'Name': 'Geeks', 'Team': 'Boston', 'Number': 3,
                        'Position': 'PG', 'Age': 33, 'Height': '6-2',
                        'Weight': 189, 'College': 'MIT', 'Salary': 99999},
                       index=[0])
# simply concatenate both dataframes
df = pd.concat([new_row, df]).reset_index(drop=True)
df.head(5)
print(df)


# ROW DELETION
# DROP() METHOD

data = pd.read_csv(r'D:\Filehandling\nba.csv',
                   encoding='latin1', index_col="Name")
data.drop(["Avery Bradley", "John Holland", "R.J. Hunter",
                            "R.J. Hunter"], inplace=True)
print(data)




