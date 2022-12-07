import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

data = {
    "calories": [420, 380, 390],
    "duration": [50, 40, 45]
}

# load data into a DataFrame object:
df = pd.DataFrame(data)

print(df)


# PANDAS EXAMPLE-01
mydataset = {
    'car': ["TATA", "MAHINDRA", "BMW"],
    'price': [100000, 5000000, 10000000]
}
myvar = pd.DataFrame(mydataset)
print(myvar)


# TO KNOW THE VERSION OF PANDAS
print(pd.__version__)


# PANDAS - SERIES- ONE DIMENSIONAL ARRAY
a = [1, 10, 20, "ANIL"]
myvar = pd.Series(a)
print(myvar)
print(myvar[0])

#SERIES - Example
ser = pd.Series()
print(ser)

data = np.array(['A', 'N', 'I', 'L'])
ser = pd.Series(data)
print(ser)

# Create Labels

num = [100, 200, "ANIL", "Daroori"]
myvar = pd.Series(a, index=["X", "Y", "Z", "W"])
print(myvar)


# Key/Values Object same like dictionaries

calories = {"day1": 500,
            "day2": 400,
            "day3": 200
            }
myvar = pd.Series(calories)
print(myvar)


# DataFrames

data = {
    "Calories": ["500", "510", "525"],
    "Duration": [50, 60, 75]
}
myvar = pd.DataFrame(data, index=["X", "Y", "Z"])
print(myvar)


# Locate ROW - DataFrame

data = {
    "Calories": ["250", "517", "575"],
    "Duration": [40, 61, 85]
}
# Load data into DataFrame Object
df = pd.DataFrame(data)
print(df)

# Locate Row
print(df.loc[0])
print(df.loc[[1, 2]])


# Named Indexes
data = {
    "car": ["ALTROZ", "BALENO", "INNOVA", "EON"],
    "company": ["TATA", "SUZUKI", "TOYOTA", "HYUNDAI"]

}
df = pd.DataFrame(data, index=["Model1", "Model2", "Model3", "Model4"])
print(df)
print(df.loc["Model1"])
print(df.loc[["Model2", "Model3"]])
print(df.loc[["Model2", "Model3", "Model4"]])


# Load Files into DataFrame
df = pd.read_csv(r'D:\Filehandling\SampleCRV.csv', encoding='latin1')
print(df)


df = pd.read_csv(r'D:\Filehandling\Data.csv', encoding='latin1')
print(df.to_string)
print(pd.options.display.max_rows)


# To Display Maximum Rows
pd.options.display.max_rows = 10000
df = pd.read_csv(r'D:\Filehandling\Data.csv', encoding='latin1')
print(df)


# PYTHON - PANDAS READ JSON
df = pd.read_json(r'D:\Filehandling\data.json', encoding='latin1')
print(df)


df = pd.read_csv(r'D:\Filehandling\Data.csv', encoding='latin1')
df.plot()
plt.show()
