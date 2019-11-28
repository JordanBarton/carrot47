#machine learning 13/09/2019
import pandas as pd
import quandl
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
import numpy as np
import matplotlib.pyplot as plt
import math
#Y4_hDsYSpwiZsAoG-21D
#quandl.ApiConfig.api_key = "YOURAPIKEY"
quandl.ApiConfig.api_key = "Y4_hDsYSpwiZsAoG-21D"


#import data
df=quandl.get('WIKI/GOOGL')


#crop data
df=df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume',]]


#work out high low %
df['HL_%']=((df['Adj. High'] - df['Adj. Close'])/df['Adj. Close']*100) 
#work out % change
df['%_change']=((df['Adj. Close']-df['Adj. Open'])/df['Adj. Open']*100)

#make new data
df=df[['Adj. Close','HL_%','%_change','Adj. Volume']]


forecast_col = 'Adj. Close'

df.fillna(-999999, inplace=True) #fill in na data

forecast_out=int(math.ceil(0.01*len(df))) #round to neareast 0.1
print(forecast_out)
#shift 
df['label']=df[forecast_col].shift(-forecast_out)
df.dropna(inplace=True)


#feature, everything except label collumn
X=np.array(df.drop(['label'],1))

#label collumn
y=np.array(df['label'])

#normalise values
X=preprocessing.scale(X)


y=np.array(df['label'])

#cut list
X_train,X_test,y_train,y_test=cross_validation.train_test_split(X,y,test_size=0.2)

#classifier
clf=LinearRegression()

clf.fit(X_train,y_train) # fit = train

accuracy = clf.score(X_test,y_test) #score = test


print(accuracy)















