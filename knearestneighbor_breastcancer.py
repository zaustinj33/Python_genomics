#-------------------------------------------------------------------------------
# Name:        module1
# Purpose:
#
# Author:      zaust
#
# Created:     11/08/2018
# Copyright:   (c) zaust 2018
# Licence:     <your licence>
#-------------------------------------------------------------------------------

import numpy as np
from sklearn import preprocessing, cross_validation, neighbors
import pandas as pd
import matplotlib.pyplot as plt
import warnings
import random
from matplotlib import style
from collections import Counter
style.use('fivethirtyeight')

#Sklearn knearest algo
"""#import dataset, replace missing data with -99999, remove id column
df = pd.read_csv('breastcancerdata.txt')
df.replace('?',-99999, inplace=True)
df.drop(['id'],1,inplace=True)

#define x and y (features and labels)
X = np.array(df.drop(['class'],1))
y = np.array(df['class'])


#Trains data set
X_train, X_test, y_train, y_test = cross_validation.train_test_split(X,y,test_size=0.2)
clf = neighbors.KNeighborsClassifier()
clf.fit(X_train, y_train)

accuracy = clf.score(X_test, y_test)
print(accuracy)

#Testing an example set          wrong dimension sizee???

example_measures = np.array([4,2,1,1,1,2,3,2])
example_measures = example_measures.reshape(-1,1)

prediction = clf.predict(example_measures)
print(prediction)    """


dataset = {'k':[[1,2],[2,3],[3,1]], 'r':[[6,5],[7,7],[8,6]]}
new_features = [5,7]

#[[plt.scatter(ii[0],ii[1],s=100,color=i) for ii in dataset[i]] for i in dataset]
#plt.scatter(new_features[0],new_features[1])
#plt.show()


#from scratch kNearest algo
#data set is larger than k, k needs to be odd to avoid ties)
def k_nearest_neighbors(data, predict, k=3):
    #return warning if  k is bigger than data set given
    if len(data) >= k:
        warnings.warm('u dumb')
    #finds euclidean distance of all points and adds them to new list
    distances = []
    for group in data:
        for features in data[group]:
            euclidean_distance = np.linalg.norm(np.array(features)-np.array(predict))
            distances.append([euclidean_distance, group])
    #counts number of votes for each dataset in dict
    votes = [i[1] for i in sorted(distances) [:k]]
    print(Counter(votes).most_common(1))
    vote_result = Counter(votes).most_common(1)[0][0]
    return vote_result

df = pd.read_csv('breastcancerdata.txt')
df.replace('?',-99999, inplace=True)
df.drop(['id'],1,inplace=True)
full_data = df.astype(float).values.tolist()
random.shuffle(full_data)

test_size = 0.2
train_set = {2:[],4:[]}
test_set = {2:[],4:[]}
train_data = full_data[:-int(test_size*len(full_data))]
test_data = full_data[:-int(test_size*len(full_data)):]

#populate dictionaries
for i in train_data:
    train_set[i[-1]].append(i[:-1])
for i in test_data:
    test_data[i[-1]].append(i[:-1])

correct = 0
total = 0

for group in test_set:
    for data in test_set[group]:
        vote = k_nearest_neighbors(train_set, data, k=5)
        if group == vote:
            correct += 1
        total += 1
print('Accuracy', correct/total)