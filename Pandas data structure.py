'''

hello there this is my solution to first Practice "no1" assigned at the 
Ultimate Python Bootcamp for Data Science & Machine Learning

'''
import pandas as pd
import numpy as np

#EX1
sample=np.linspace(1,10)
ser=pd.Series(sample)
print(ser)
ser1=pd.Series(np.random.rand(3),index=[1,2,3])
print(ser1)
#EX2
listt=[1,2,3,4]
ser2=pd.Series(listt)
print(ser2)
#EX3
mere={'India':'New Delhi','Japan':'Tokyo','UK':'Lindon'}
ser3=pd.Series(mere)
print(ser3)
print(ser3.index)
print(ser3.values)
#EX4
values = np.arange(10) #must match the values & index
ser4=pd.Series(values,index=['A','B','C','D','E','F','G','H','I','J'])
print(ser4)
#EX5
print(ser4.shape)
print(ser4.size )
#EX6
print(ser4.index[4::3])
print(ser4.index[::-1])
print(ser4.index[::2])
#EX7
print(ser4.tolist())
#EX8
ser5=pd.Series([25,50,100,200,300,400])
ser6=pd.Series([500,600,700])
print(ser5.append(ser6)) #print(ser5.union(ser6)) OR print(ser5|ser6)
#EX9
ser7 =ser5.append(ser6)
valuesgraterthan= ser7 >=100 
print(ser7[valuesgraterthan])
#EX10
exam_data  = {
'name': ['Arun', 'Rama', 'Kantharaj', 'James', 'Emily', 'Michael','Matthew', 'Laura', 'Kevin', 'Jonas'], 
'score': [12, 10, 17, np.nan, 9, 30, 15, np.nan, 8, 19],
'attempts': [1, 3, 2, 3, 2, 3, 1, 1, 2, 1],
'qualify': ['yes', 'no', 'yes', 'no', 'no', 'yes', 'yes', 'no', 'no', 'yes']
}
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j']
dframe = pd.DataFrame(exam_data, index= labels)
print(dframe.info())
#EX11
scoregraterthan = (dframe['score']>12)
print(dframe.loc[scoregraterthan])
print("people with a score \n",dframe['score'].notnull())
print("people without a scor\n", dframe['score'].isnull())
#EX12
didqualify = dframe['qualify']=='yes'
print(dframe.loc[didqualify])
didntqualify = dframe['qualify']=='no'
print(dframe.loc[didntqualify])
#EX13
dframe2 = dframe[['name','attempts','qualify']]
print(dframe2)
#EX14
print(len(dframe.loc[dframe['attempts']==1])) 
# OR print(exam_data['attempts'].values_counts())
#EX15
highest = dframe['score']
print(highest.max())
