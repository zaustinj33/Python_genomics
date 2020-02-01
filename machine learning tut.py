#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     01/08/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

#Machine Learning tutorials

# Regression
import math, datetime
import pandas  as pd
import quandl
import numpy as np
from sklearn import preprocessing, cross_validation, svm
from sklearn.linear_model import LinearRegression
quandl.ApiConfig.api_key = 'ayjtqt6zUTdFY25xKQAx'
df = quandl.get('WIKI/GOOGL'  )
import matplotlib.pyplot as plt
from matplotlib import style
import pickle

style.use('ggplot')


df = df[['Adj. Open','Adj. High','Adj. Low','Adj. Close','Adj. Volume']]
df['HL_PCT'] = (df['Adj. High']-df['Adj. Close'])/df['Adj. Close']  *100
df['PCT_change'] = (df['Adj. Close']-df['Adj. Open'])/df['Adj. Open'] *100

df = df[['Adj. Close', 'HL_PCT','PCT_change','Adj. Volume']]

forecast_col = 'Adj. Close'
df.fillna(-99999, inplace=True)

# shifts prediction values n times total length of data set
forecast_out = int(math.ceil(0.01*len(df)))

df['label'] = df[forecast_col].shift(-forecast_out)


# X is common for Features (dep variable)
# Y is common for Labels (indep variable)
X = np.array(df.drop(['label'],1))
X = preprocessing.scale(X)
X_lately = X[-forecast_out:]
X = X[:-forecast_out:]

df.dropna(inplace=True)
y = np.array(df['label'])

# define training algo (in this case cross_validation)
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X, y, test_size = 0.2)

# defining classifier (clf) based on linear regression (can switch to others)
clf = LinearRegression(n_jobs=-1)
clf.fit(X_train, y_train)

#saves classifier
#with open('linearregression.pickle', 'wb') as f:
    #pickle.dump(clf, f)
#reloads classifier
pickle_in = open('linearregression.pickle', 'rb')
clf = pickle.load(pickle_in)


accuracy = clf.score(X_test, y_test)

forecast_set = clf.predict(X_lately)
print(forecast_set, accuracy, forecast_out)

#print(accuracy)

#set up graph with dates
df['Forecast'] = np.nan
last_date = df.iloc[-1].name
last_unix = last_date.timestamp()
one_day = 86400
next_unix = last_unix + one_day

# Iterate through X and Y
for i in forecast_set:
    next_date = datetime.datetime.fromtimestamp(next_unix)
    next_unix += one_day
    df.loc[next_date] = [np.nan for _ in range(len(df.columns)-1)] + [i]

# Graph labels
df['Adj. Close'].plot()
df['Forecast'].plot()
plt.legend(loc=4)
plt.xlabel('Date')
plt.ylabel('Price')
plt.show()






