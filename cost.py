import numpy as np
import pandas as pd
import re
from pandas import ExcelWriter
from re import S
import matplotlib.pyplot as plt



labels = 'Raw materials', 'Packaging', 'Others', 'Variable Manufacturing', 'Fixed Manufacturing', 'Warehouse', 'Primary Transportation', 'Delivery Transportation'
sizes = [36.85, 31.48, 2.56, 5.97, 13.94, 2.55, 1.40, 5.25]
explode = (0.2, 0.2, 0.2, 0, 0, 0, 0, 0)  # only "explode" the 2nd slice (i.e. 'Hogs')
fig1, ax1 = plt.subplots()
ax1.pie(sizes, explode=explode, labels=labels, autopct='%1.1f%%',
        shadow= True, startangle=60)
ax1.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
plt.title("Cost components")
plt.legend(loc="upper left")
plt.show()