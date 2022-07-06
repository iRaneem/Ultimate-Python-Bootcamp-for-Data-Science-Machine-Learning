# -*- coding: utf-8 -*-

# -- Sheet --

import pandas as pd

data=pd.read_csv('ititanic.csv')

data.columns.values

data.columns.to_list()

data.head(10)

data.tail(10)

data.info()

data.isnull().sum()

data.describe()

data[data['sex']=='male'].value_counts()

data[data['sex']=='female'].value_counts()

data.sex.value_counts()

len(data[data['age']>=50])

len(data[data['age']<50])

data.survived.value_counts()

len(data[(data['survived']==1)&(data['sex']=='male')])

len(data[(data['survived']==1)&(data['sex']=='female')])

data.columns.to_list()

data.to_csv('modified_titanic.csv',columns=
['survived',
 'pclass',
 'sex',
 'age',
 'sibsp',
 'fare',
 'embarked',])

import csv
import pandas as pd

with open(r"data\nba.csv") as csv_file:
 csv_reader=csv.reader(csv_file,delimiter=',')
df=pd.DataFrame([csv_reader],index=None)

for val in list(df[1]):
    print(val)

