'''

hello there this is my solution to seconed Practice "no2" assigned at the 
Ultimate Python Bootcamp for Data Science & Machine Learning

'''
import pandas as pd
import numpy as np
exam_data  = {'name': ['Anjum', 'Anali', 'Souria', 'Rockea', 'Imani', 'Mouliya', 'Julie', 'Rana', 'Kavin', 'Bosia'],
               'score': [15.5, 9, 16.5, np.nan, 9, 30, 17.5, np.nan, 8, 20], 
               'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
#EX1
Data=pd.DataFrame(exam_data,index=labels)
print(Data.iloc[:4])
#EX2
print(Data.loc[['A','C','E','G'],['score','attempts']])#Explicit
print(Data.iloc[[1,3,5,7],[1,2]]) #implicit
print('number of rows are : ',len(Data))
print('number of columns are : ',len(Data.axes[1]))
selection=Data['score'].between(16,20)
print(Data.loc[selection])
print(Data.loc[(Data['attempts']<2) & (Data['score']>16)])
#EX3
Data.loc[['C','I'],'score']=16
print(Data)
print(sum(Data['attempts']))
Data.loc['K']=['Rupali',16,2,'yes']
print('after adding a new row : \n',Data)
Data.drop('K', inplace=True)
print('after removing last added row : \n',Data)
new=pd.DataFrame(Data[:-4])
print('the new frame is :\n',new)