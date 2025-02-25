import numpy as np
import scipy

array = np.array([[1, 1, 3, 3, 4, 4, 4, 5, 7, 7, 8, 9, 12]])

mean   = np.mean(array)
median = np.median(array)
mode   = scipy.mode(array)

print(f'Mean = ', mean)
print(f'Median = ', median)
print(f'Mode = ', mode)



Program7.py

#Generating random floating-point numbers between 0 and 1

# Explanation: Using np.random.rand() to create a random array of given shape

random_data = np.random.rand(3, 4) # Creates a 3x4 array with random values
print(random_data)
-------------------------------------------------------
program8.py

import math

user_number = int(input('Enter a number of your choice between [0 and 9]: '))
system_number = math.random(10)
if system_number == user_number:
	print('CrorePati')
else:
	print('RoadPati')
-------------------------------------------------------
import pandas as pd

def read_excel_file():
    #Define the path to the Excel file
    file_path = './students.xlsx'

    # Read the Excel file into a pandas DataFrame
    df = pd.read_excel(file_path)

	# Display the first few rows of the DataFrame
    print(df.count())
    print(df.head())
    print(df.tail())

def read_excel_file1():
    file_path = './students.xlsx'
    df = pd.read_excel(file_path)
    for index, row in df.iterrows():
        print(row[0], '  ', row[1])

def read_excel_file2():
    file_path = './students.xlsx'
    df = pd.read_excel(file_path)
    for row in df.iterrows():
       print(row[1][0], row[1][1])