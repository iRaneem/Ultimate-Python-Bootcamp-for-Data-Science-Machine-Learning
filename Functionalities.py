'''

hello there this is my solution to third Practice "no3" assigned at the 
Ultimate Python Bootcamp for Data Science & Machine Learning

'''
import pandas as pd 
import numpy as np 
exam_data  = {'name': ['Anjum', 'Anali', 'Souria', 'Rockea', 'Imani', 'Mouliya', 'Julie', 'Rana', 'Kavin', 'Bosia'],
               'score': [15.5, 9, 16.5, np.nan, 9, 30, 17.5, np.nan, 8, 20], 
               'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
              'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']} 
labels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
data =pd.DataFrame (exam_data, index = labels)
print (data)
#EX1
print (data.sort_values('name', ascending = False))
print (data.sort_values('attempts', ascending = True))
print (data.drop('attempts', axis = 1))
print (data.reindex (columns =['name', 'attempts', 'score', 'qualify']))
print (data.reindex (['A', 'C', 'B', 'E', 'D']))
#EX2
f = lambda x: x.max()
print(data[['score','attempts']].apply(f))
def f2(x): return pd.Series([x.max(),x.min(),x.mean()],index=['max','min','mean'])
print(data[['score','attempts']].apply(f2))
print(data.sort_index(ascending=False))
print(data.sort_values(by=['score'],axis=0))
print(data.sort_values(by=['attempts'],axis=0))
#EX3
print(data[['score','attempts']].rank(method='first', numeric_only=True))
print(data[['score','attempts']].idxmax())
print(data[['score','attempts']].count())
print(data[['score','attempts']].apply(pd.value_counts))