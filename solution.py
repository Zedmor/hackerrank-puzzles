import pandas as pd
import matplotlib.pyplot as plt
from matplotlib import style
style.use('fivethirtyeight')

# Building data frame for historical data of stocks

df = pd.read_csv('stocksdata.csv', header=None, delim_whitespace=True, index_col=0).T

df.reset_index(drop=True, inplace=True)

#print(df.head())
# print(".......")
# print(df.tail())

# End building data frame for historical data of stocks

# Converting data values to percent change form

for i in df:
    df[i] = (df[i] - df[i][0]) / df[i][0] * 100.0

#print(df.head())

# End converting data values to percent change form

# Summary stats and correlations

print("Summary Stats")
print(df.describe())

print("")
print(df.corr())

# End summary stats

# Plotting historical stock data

df[['UCB','UCSC']].plot()
#plt.show()

#for i in range(5,len(df['UCB'])):

from operator import sub

def isPos(x):
    if x>0: return(1)
    else: return(0)

df_labels=df.copy()

for i in df:
    df_labels[i]=[0]+list(list(map(sub,df[i][1:],df[i])))

import numpy as np
import seaborn as sns
sns.set(color_codes=True)
np.random.seed(sum(map(ord, "distributions")))

sns.pairplot(df)

from sklearn import svm
from sklearn import cross_validation
clf = svm.SVC(probability=True)

#X_train, X_test,y_train,y_test = cross_validation.train_test_split(df,df_labels['UCB'], test_size=0.2,random_state=0)

import random
ran=random.randrange(400)

X_train = df[:ran]
X_test = df[ran+1:]

y_train = df_labels['RIT'][:ran]
y_test = df_labels['RIT'][ran+1:]

len(y_train)
y_train.head()
clf.fit(X_train,y_train)


pred=clf.predict(X_test)

from sklearn.metrics import accuracy_score
print(accuracy_score(pred,y_test))



y_pred_prob = clf.predict_proba(X_test)
#t_pred_prob = clf.predict_proba(T)


from sklearn import metrics
for z in range(0,100,5):
    y_pred = []
    for i in range(len(X_test)):
        if y_pred_prob[i][0]>=z/100:
            y_pred.append(False)
        else: y_pred.append(True)

    print('Cutoff is',z,'F1 score:',metrics.f1_score(y_test, y_pred))

#t_pred = clf.predict(T)




df_labels.head()
len(df_labels['UCB'])

len(list(map(isPos,list(map(sub,df['UCB'][1:-1],df['UCB'])))))

# End plotting historical stock data

