# -*- coding: utf-8 -*-
"""
Created on Tue May  7 21:00:16 2019

@author: superuser
"""

import numpy as np
import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import csv
from sklearn import preprocessing

pd.set_option("display.max_rows", 1000)    #設定最大能顯示1000rows
pd.set_option("display.max_columns", 1000) #設定最大能顯示1000columns

#讀取資料
raw_csv = pd.read_csv('file_path')
##pandas內建的onehot
#data_dum = pd.get_dummies(raw_csv)
#data_dum = pd.DataFrame(data_dum)

#label encoder to convert string data to categorical
le = preprocessing.LabelEncoder()
raw_csv.County = le.fit_transform(raw_csv.County)
raw_csv.Location = le.fit_transform(raw_csv.Location)
data_dum = raw_csv

#print(data_dum.iloc[:, 1:])
plt.figure(figsize=(25, 20))
svm = sns.heatmap(data_dum.iloc[:, 1:].corr(),annot = True )


corr = data_dum.iloc[:, 1:].corr()

figure = svm.get_figure()    
figure.savefig('output2.pdf', bbox_inches='tight')

plt.show()



corr.to_csv('output.csv',index=0,
                            quotechar='"',
                            quoting=csv.QUOTE_NONNUMERIC) #csv 不保留index 不留小數位