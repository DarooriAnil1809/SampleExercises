import pandas as pd


# How to Get Column Names in Pandas DataFrame
# Method 1
data = pd.read_csv(r'D:\Filehandling\nba.csv', encoding='latin1')
for col in data.columns:
    print(col)

# Method 2 -using column attribute with dataframe object
data = pd.read_csv(r'D:\Filehandling\nba.csv', encoding='latin1')
list(data.columns)


# Method 3 -using keys function
data = pd.read_csv(r'D:\Filehandling\nba.csv', encoding='latin1')
print(data.keys())

# Method 4 - using column.values method
data = pd.read_csv(r'D:\Filehandling\nba.csv', encoding='latin1')
list(data.columns.values)

# Method 5 - Sorted() Method
data = pd.read_csv(r'D:\Filehandling\nba.csv', encoding='latin1')
df = sorted(data)
print(df)


# DROP COLUMNS in DATAFRAME
data = {
    'TATA': ['ALTROZ', 'NANO', 'NEXON', 'INDICA'],
    'TOYOTA': ['INNOVA', 'FORTUNER', 'GLANZA', 'CRYSTA'],
    'MARUTI': ['ALTO', 'WAGONR', 'BREEZA', 'BALENO'],
    'HYUNDAI': ['EON', 'VERNA', 'SANTRO', 'I20'],
    'RENAULT': ['KWID', 'TRIBER', 'KIGER', 'LIGER']
}

df = pd.DataFrame(data)
print(df)

# TO REMOVE SPECIFIC COLUMN
data = {
    'TATA': ['ALTROZ', 'NANO', 'NEXON', 'INDICA'],
    'TOYOTA': ['INNOVA', 'FORTUNER', 'GLANZA', 'CRYSTA'],
    'MARUTI': ['ALTO', 'WAGONR', 'BREEZA', 'BALENO'],
    'HYUNDAI': ['EON', 'VERNA', 'SANTRO', 'I20'],
    'RENAULT': ['KWID', 'TRIBER', 'KIGER', 'LIGER']
}

df = pd.DataFrame(data)
removecolu = df.drop(['RENAULT'], axis=1)
print(removecolu)

# TO REMOVE SPECIFIC(MULTIPLE COLUMNS)
data = {
    'TATA': ['ALTROZ', 'NANO', 'NEXON', 'INDICA'],
    'TOYOTA': ['INNOVA', 'FORTUNER', 'GLANZA', 'CRYSTA'],
    'MARUTI': ['ALTO', 'WAGONR', 'BREEZA', 'BALENO'],
    'HYUNDAI': ['EON', 'VERNA', 'SANTRO', 'I20'],
    'RENAULT': ['KWID', 'TRIBER', 'KIGER', 'LIGER']
}

df = pd.DataFrame(data)
removecolu = df.drop(['RENAULT', 'MARUTI'], axis=1)
print(removecolu)

# TO REMOVE COLUMNS BASED ON COLUMN INDEX
data = {
    'TATA': ['ALTROZ', 'NANO', 'NEXON', 'INDICA'],
    'TOYOTA': ['INNOVA', 'FORTUNER', 'GLANZA', 'CRYSTA'],
    'MARUTI': ['ALTO', 'WAGONR', 'BREEZA', 'BALENO'],
    'HYUNDAI': ['EON', 'VERNA', 'SANTRO', 'I20'],
    'RENAULT': ['KWID', 'TRIBER', 'KIGER', 'LIGER']
}

df = pd.DataFrame(data)
removecolu = df.drop(df.columns[[1]], axis=1, inplace=True)
print("REMOVE COLUMNS BASED ON COLUMN INDEX")
print(removecolu)


# x = input("Type a number: ")
# y = input("Type another number: ")

# sum = int(x) + int(y)

# print("The sum is: ", sum)


# Read csv files using Pandas.Read_csv()
# Syntax
# pd.read_csv(filepath,sep='',header='infer',index_col=None,usecols=None,engine=None,nrows=None)
print("Print the NBA FILE")
data = pd.read_csv(r'D:\Filehandling\nba.csv', encoding='latin1')
print(data)


# usecols in read_csv - read/load specific columns
# purpose - Load the specific Columns
# Name,Team,Salary
print("Load Specific Columns - NAME,TEAM,SALARY")
data = pd.read_csv(r'D:\Filehandling\nba.csv', encoding='latin1',
                   header=0, usecols=["Name", "Team", "Salary"])
print(data)


# using index_col in read_csv()
# purpose - reindex the header using the above function
print("REINDEX THE HEADER")
data = pd.read_csv(r'D:\Filehandling\nba.csv', encoding='latin1', header=0,
                   index_col=["Name", "Salary"],
                   usecols=["Name", "Team", "Salary"])
print(data)

# using nrows in read_csv()
# purpose - Display only 5 Rows

data = pd.read_csv(r'D:\FileHandling\nba.csv', encoding='latin1',
                   header=0, usecols=["Name", "Team", "Salary"],
                   index_col=["Name", "Salary"],
                   nrows=2)
print(data)


# using skiprows()
# purpose - Skip some rows in csv file
#skiprows = [1,12]

data = pd.read_csv(r'D:\FileHandling\nba.csv', encoding='latin1',
                   header=0, usecols=["Name", "Team", "Salary"],
                   skiprows=[1])

print(data)


# Saving a PANDAS DATAFRAME AS A CSV

# List data
name = ['ANIL', 'Virat', 'Yuvraj', 'Peter Dinklage']
deg = ['BTECH', 'MBA', 'MCA', 'BCOM']
score = [80, 90, 78, 88]

# Dict of lists

dict = {'Name': name,
        'Degree': deg,
        'Score': score
        }
df = pd.DataFrame(dict)
df.to_csv(r'D:\Filehandling\profiledata.csv', encoding='latin1')
print("DICT TO DATAFRAME")
print(df)


# HOW TO APPEND PANDAS DATAFRAME TO EXISTING CSV FILE
# SYNTAX
#df.to_csv('Existing CSV FILE', Mode= 'a', index = False, header = False)

data = {
    'Name': ['Jadeja', 'Arshadeep', 'Shami', 'Bumrah'],
    'Runs': [25, 10, 5, 0],
    'Wickets': [1, 2, 1, 2],
    'Catch': [1, 0, 1, 0]
}
df = pd.DataFrame(data)
df.to_csv(r'D:\Filehandling\Append.csv', encoding='latin1',
          mode='a', index=False, header=False)
print("Data Append Successfully")
