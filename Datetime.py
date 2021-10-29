import numpy as np
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


df = read_xlsx("Data_clean")
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

s1 = float(0)
s2 = float(0)
s3 = float(0)
s4 = float(0)
s5 = float(0)
s6 = float(0)
s7 = float(0)
s8 = float(0)
s9 = float(0)
s10 = float(0)
s11 = float(0)
s12 = float(0)

n1 = float(0)
n2 = float(0)
n3 = float(0)
n4 = float(0)
n5 = float(0)
n6 = float(0)
n7 = float(0)
n8 = float(0)
n9 = float(0)
n10 = float(0)
n11 = float(0)
n12 = float(0)

for i in range(2, 13635):
    if(str(dl[i][3]).find("Central",0,len(str(dl[i][3])))!=-1):
        if(((dl[i][1]).find("12",0,len(dl[i][1]))!=-1)):
            c12 += float(dl[i][4])
        if(((dl[i][1]).find("11",0,len(dl[i][1]))!=-1)):
            c11 += float(dl[i][4])
        if(((dl[i][1]).find("10",0,len(dl[i][1]))!=-1)):
            c10 += float(dl[i][4])
        if(((dl[i][1]).find("9",0,len(dl[i][1]))!=-1)):
            c9 += float(dl[i][4])
        if(((dl[i][1]).find("8",0,len(dl[i][1]))!=-1)):
            c8 += float(dl[i][4])
        if(((dl[i][1]).find("7",0,len(dl[i][1]))!=-1)):
            c7 += float(dl[i][4])
        if(((dl[i][1]).find("6",0,len(dl[i][1]))!=-1)):
            c6 += float(dl[i][4])
        if(((dl[i][1]).find("5",0,len(dl[i][1]))!=-1)):
            c5 += float(dl[i][4])
        if(((dl[i][1]).find("4",0,len(dl[i][1]))!=-1)):
            c4 += float(dl[i][4])
        if(((dl[i][1]).find("3",0,len(dl[i][1]))!=-1)):
            c3 += float(dl[i][4])
        if(((dl[i][1]).find("2",0,len(dl[i][1]))!=-1) and ((dl[i][1]).find("12",0,len(dl[i][1]))==-1) ):
            c2 += float(dl[i][4])
        if(((dl[i][1]).find("1",0,len(dl[i][1]))!=-1) and ((dl[i][1]).find("11",0,len(dl[i][1]))==-1) and ((dl[i][1]).find("10",0,len(dl[i][1]))==-1)):
            c1 += float(dl[i][4])
    if(str(dl[i][3]).find("South",0,len(str(dl[i][3])))!=-1):
        if(((dl[i][1]).find("12",0,len(dl[i][1]))!=-1)):
            s12 += float(dl[i][4])
        if(((dl[i][1]).find("11",0,len(dl[i][1]))!=-1)):
            s11 += float(dl[i][4])
        if(((dl[i][1]).find("10",0,len(dl[i][1]))!=-1)):
            s10 += float(dl[i][4])
        if(((dl[i][1]).find("9",0,len(dl[i][1]))!=-1)):
            s9 += float(dl[i][4])
        if(((dl[i][1]).find("8",0,len(dl[i][1]))!=-1)):
            s8 += float(dl[i][4])
        if(((dl[i][1]).find("7",0,len(dl[i][1]))!=-1)):
            s7 += float(dl[i][4])
        if(((dl[i][1]).find("6",0,len(dl[i][1]))!=-1)):
            s6 += float(dl[i][4])
        if(((dl[i][1]).find("5",0,len(dl[i][1]))!=-1)):
            s5 += float(dl[i][4])
        if(((dl[i][1]).find("4",0,len(dl[i][1]))!=-1)):
            s4 += float(dl[i][4])
        if(((dl[i][1]).find("3",0,len(dl[i][1]))!=-1)):
            s3 += float(dl[i][4])
        if(((dl[i][1]).find("2",0,len(dl[i][1]))!=-1) and ((dl[i][1]).find("12",0,len(dl[i][1]))==-1) ):
            s2 += float(dl[i][4])
        if(((dl[i][1]).find("1",0,len(dl[i][1]))!=-1) and ((dl[i][1]).find("11",0,len(dl[i][1]))==-1) and ((dl[i][1]).find("10",0,len(dl[i][1]))==-1)):
            s1 += float(dl[i][4])
    if(str(dl[i][3]).find("North",0,len(str(dl[i][3])))!=-1):
        if(((dl[i][1]).find("12",0,len(dl[i][1]))!=-1)):
            n12 += float(dl[i][4])
        if(((dl[i][1]).find("11",0,len(dl[i][1]))!=-1)):
            n11 += float(dl[i][4])
        if(((dl[i][1]).find("10",0,len(dl[i][1]))!=-1)):
            n10 += float(dl[i][4])
        if(((dl[i][1]).find("9",0,len(dl[i][1]))!=-1)):
            n9 += float(dl[i][4])
        if(((dl[i][1]).find("8",0,len(dl[i][1]))!=-1)):
            n8 += float(dl[i][4])
        if(((dl[i][1]).find("7",0,len(dl[i][1]))!=-1)):
            n7 += float(dl[i][4])
        if(((dl[i][1]).find("6",0,len(dl[i][1]))!=-1)):
            n6 += float(dl[i][4])
        if(((dl[i][1]).find("5",0,len(dl[i][1]))!=-1)):
            n5 += float(dl[i][4])
        if(((dl[i][1]).find("4",0,len(dl[i][1]))!=-1)):
            n4 += float(dl[i][4])
        if(((dl[i][1]).find("3",0,len(dl[i][1]))!=-1)):
            n3 += float(dl[i][4])
        if(((dl[i][1]).find("2",0,len(dl[i][1]))!=-1) and ((dl[i][1]).find("12",0,len(dl[i][1]))==-1) ):
            n2 += float(dl[i][4])
        if(((dl[i][1]).find("1",0,len(dl[i][1]))!=-1) and ((dl[i][1]).find("11",0,len(dl[i][1]))==-1) and ((dl[i][1]).find("10",0,len(dl[i][1]))==-1)):
            n1 += float(dl[i][4])
         
ct =[c1, c2, c3, c4, c5, c6, c7, c8, c9, c10, c11, c12]
s= [s1, s2, s3, s4, s5, s6, s7, s8, s9, s10, s11, s12]
n= [n1, n2, n3, n4, n5, n6, n7, n8, n9, n10, n11, n12]

print(n)
print(s)
print(ct)

N=12
plt.style.use("ggplot")
plt.figure()
plt.plot(np.arange(0, N), s, label="North")
plt.plot(np.arange(0, N), ct, label="Center")
plt.plot(np.arange(0, N), n, label="South")
plt.title("Timeseries of Sales Volume")
plt.xlabel("Month")
plt.ylabel("Rc")
plt.legend(loc="lower left")
plt.show()

Dd.to_excel("plot1.xlsx", index= True)