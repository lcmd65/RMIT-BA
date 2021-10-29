import numpy as np
import pandas as pd
import re
from pandas import ExcelWriter
from re import S
import matplotlib.pyplot as plt

C_T = 23000
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
df.columns = ('Period', 'Product Type', 'SO', 'SV', 'GS', 'RM', 'Packaging', 'ODC', 'VM', 'FM', 'Warehouse', 'Trans_P', 'Trans_D')

dt=(df['Period'].value_counts())

dl= df.to_numpy()
x= dict()

sumY3 = float(0)
sum1 = float(0)
RGBCF = float(0)
RGBHF = float(0)
CANCF = float(0)
CANHF = float(0)
PETCF = float(0)
PETHF = float(0)
Water = float(0)
PMX = float(0)

for i in range(1, 13635):
   if(((dl[i][0]).find("Y3",0,len(dl[i][0]))!=-1) or ((dl[i][0]).find("Y03",0,len(dl[i][0]))!=-1) ):
        sumY3 += float(dl[i][3])
        if(dl[i][1]=="RGB CF"):
            RGBCF += float(dl[i][3])
        if(dl[i][1]=="RGB HF"):
            RGBHF += float(dl[i][3])    
        if(dl[i][1]=="CAN CF"):
            CANCF += float(dl[i][3])
        if(dl[i][1]=="CAN HF"):
            CANHF += float(dl[i][3])
        if(dl[i][1]=="PET CF"):
            PETCF += float(dl[i][3])
        if(dl[i][1]=="PET HF"):
            PETHF += float(dl[i][3])
        if(dl[i][1]=="Water"):
            Water += float(dl[i][3])
        if(dl[i][1]=="PMX"):
            PMX += float(dl[i][3])

print('Total sales Vol Y3',sumY3)    

t= [RGBCF, RGBHF, CANCF, CANHF,PETCF, PETHF,Water, PMX]
print(t)

sum1 = float(0)
RGBCF = float(0)
RGBHF = float(0)
CANCF = float(0)
CANHF = float(0)
PETCF = float(0)
PETHF = float(0)
Water = float(0)
PMX = float(0)

for i in range(0, 13633):
    if(((dl[i][0]).find("Y3",0,len(dl[i][0]))!=-1) or ((dl[i][0]).find("Y03",0,len(dl[i][0]))!=-1)):
        sum1 += float(dl[i][4])/C_T
        if(dl[i][1]=="RGB CF"):
            RGBCF += float(dl[i][4])/C_T
        if(dl[i][1]=="RGB HF"):
            RGBHF += float(dl[i][4])/C_T  
        if(dl[i][1]=="CAN CF"):
            CANCF += float(dl[i][4])/C_T
        if(dl[i][1]=="CAN HF"):
            CANHF += float(dl[i][4])/C_T
        if(dl[i][1]=="PET CF"):
            PETCF += float(dl[i][4])/C_T
        if(dl[i][1]=="PET HF"):
            PETHF += float(dl[i][4])/C_T
        if(dl[i][1]=="Water"):
            Water += float(dl[i][4])/C_T
        if(dl[i][1]=="PMX"):
            PMX += float(dl[i][4])/C_T

u= [RGBCF, RGBHF, CANCF, CANHF,PETCF, PETHF,Water, PMX]

Z = t
print(u)
a= pd.DataFrame(t,u)

a.to_excel('cal.xlsx', index = True)

plt.bar(range(len(t)), Z , align= 'center')
plt.xticks(range(len(t)), ['RGBCF', 'RGBHF', 'CANCF', 'CANHF','PETCF', 'PETHF','Water', 'PMX'])
plt.title('Sales Volume')
plt.show()