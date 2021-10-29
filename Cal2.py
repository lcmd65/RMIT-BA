import numpy as np
from array import array
import pandas as pd
import datetime 
import re
from re import S
from pandas import ExcelWriter
import seaborn as sns
import matplotlib.pyplot as plt

def read_xlsx(name):
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


df = read_xlsx("data_month")
dl= df.to_numpy()

c1 = float(0)
c2 = float(0)
c3 = float(0)
c4 = float(0)
c5 = float(0)
c6 = float(0)
c7 = float(0)
c8 = float(0)
c9 = float(0)
c10 = float(0)
c11 = float(0)
c12 = float(0)

RGBCF = []
RGBHF = []
CANCF = []
CANHF = []
PETCF = []
PETHF = []
Water = []
PMX = []
for i in range(12):
    RGBCF.append(0)
    RGBHF.append(0)
    CANCF.append(0)
    CANHF.append(0)
    PETCF.append(0)
    PETHF.append(0)
    Water.append(0)
    PMX.append(0)
for i in range(2, 13635):
        if(((str(dl[i][1]).find("12",0,len(str(dl[i][1])))!=-1))):
            c12 += float(dl[i][3])
        if(((str(dl[i][1]).find("11",0,len(str(dl[i][1])))!=-1))):
            c11 += float(dl[i][3])
        if(((str(dl[i][1]).find("10",0,len(str(dl[i][1])))!=-1))):
            c10 += float(dl[i][3])
        if(((str(dl[i][1]).find("9",0,len(str(dl[i][1])))!=-1))):
            c9 += float(dl[i][3])
        if(((str(dl[i][1]).find("8",0,len(str(dl[i][1])))!=-1))):
            c8 += float(dl[i][3])
        if(((str(dl[i][1]).find("7",0,len(str(dl[i][1])))!=-1))):
            c7 += float(dl[i][3])
        if(((str(dl[i][1]).find("6",0,len(str(dl[i][1])))!=-1))):
            c6 += float(dl[i][3])
        if(((str(dl[i][1]).find("5",0,len(str(dl[i][1])))!=-1))):
            c5 += float(dl[i][3])
        if(((str(dl[i][1]).find("4",0,len(str(dl[i][1])))!=-1))):
            c4 += float(dl[i][3])
        if(((str(dl[i][1]).find("3",0,len(str(dl[i][1])))!=-1))):
            c3 += float(dl[i][3])
        if(((str(dl[i][1]).find("2",0,len(str(dl[i][1])))!=-1)) and ((str(dl[i][1])).find("12",0,len(str(dl[i][1])))==-1) ):
            c2 += float(dl[i][3])
        if(((str(dl[i][1]).find("1",0,len(dl[i][1]))!=-1)) and (str(dl[i][1]).find("11",0,len(str(dl[i][1]))==-1)) and (str(dl[i][1]).find("10",0,len(str(dl[i][1]))==-1))):
            c1 += float(dl[i][3])





ct =[c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
print(ct)

