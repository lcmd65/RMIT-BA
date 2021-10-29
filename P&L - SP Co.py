import numpy as np
import pandas as pd
import re
from pandas import ExcelWriter
from re import S
import matplotlib.pyplot as plt

C_T = 0.000044
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

df = read_only("Data_clean")
df = delete_row1(df)


dl= df.to_numpy()
x= dict()
RM = float(0)
PA = float(0)
OS = float(0)
TPC = float(0)
VM = float(0)
FM = float(0)
WH = float(0)
PT = float(0)
DT = float(0)

for i in range(2, 13633):
    if(((dl[i][1]).find("Y3",0,len(dl[i][1]))!=-1) or ((dl[i][1]).find("Y03",0,len(dl[i][1]))!=-1) ):
       RM += float(dl[i][6])*C_T
       PA += float(dl[i][7])*C_T
       OS += float(dl[i][8])*C_T
       VM += float(dl[i][9])*C_T
       FM += float(dl[i][10])*C_T
       WH += float(dl[i][11])*C_T
       PT += float(dl[i][12])*C_T
       DT += float(dl[i][13])*C_T

t= [RM ,PA , OS, VM, FM, WH, PT, DT]

a= pd.DataFrame(t) 
a.to_excel('cal.xlsx', index = True)
print(a)

plt.plot(t)
plt.show()