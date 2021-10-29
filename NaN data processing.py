import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import re
from pandas import ExcelWriter
from re import S

# function

def read_xlsx(name):
    xl = pd.ExcelFile(name+'.xlsx')
    data = pd.read_excel(xl, 0, header=None)
    print(data)     
    data = data.to_numpy()
    return data

def read_only(name):
    xl = pd.ExcelFile(name+'.xlsx')
    data = pd.read_excel(xl, 0, header=None)
    return data

def delete_row1(name):
    name.drop(name.index[:1], inplace=True)
    return name

def delete_column(name,cl_name):
    name.drop(cl_name, axis=1, inplace=True)
    return name
    

def data_fill(name,column):
    name[column] = name[column].replace(np.nan, 0)

def data_fillall(name):
    name = name.replace(np.nan, 0)

# main

df = read_xlsx("Data")
num = read_only("Data")

for i in range(0,2):
    num = delete_row1(num)
    
for i in range(0,3):
    num = delete_column(num,i+13)
    
for i in range(0,num.shape[1]):
    data_fill(num,i)

num = num.dropna(how='any',axis=0)
print(num)
num.describe()

with pd.ExcelWriter('Round 1 Dataset.xlsx', mode='a') as writer:
    num.to_excel(writer, sheet_name='data_clean', index=False)