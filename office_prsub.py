import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#f = open('office.txt','r')

#Read training dataset
#F,N = map(int, input().split())
F,N = map(int, input().split())
featlist = []
for i in range (F):
    featlist.append('F'+str(i))
featlist.append('y')
df_train = pd.DataFrame(columns=featlist)
for i in range(N):
    #a = [int(x) for x in input().split()]
    a = [float(x) for x in input().split()]
    #print(a)
    df_train=df_train.append(dict(zip(featlist,a)),ignore_index=True)

#Read test dataset
y_n = int(input())
######df_test = pd.DataFrame(columns=featlist[:-1])

for i in range(y_n):
    a = [float(x) for x in input().split()]
    df_train = df_train.append(dict(zip(featlist[:F],a)),ignore_index=True)
#print(df_train)
# for i in range(N):
#     arr =  map(float,input().split())
#     print(arr)
# print(df_train)
# print (df_test)

#df_train.insert(0,'intercept',[1]*(y_n+N))
#featlist=['intercept']+featlist
result = make_pipeline(PolynomialFeatures(F), Ridge())
result.fit(df_train[featlist[:-1]][:-y_n],list(df_train['y'][:-y_n]))
# y_plot = result.predict(X_plot)
# plt.plot(x_plot, y_plot, label="degree %d" % degree)
#
# plt.legend(loc='lower left')
#
#plt.show()
#result = sm.OLS(list(df_train['y'][:-y_n]),df_train[featlist[:-1]][:-y_n],axis=1).fit()
#result.fit()

predict=result.predict(df_train[featlist[:-1]][-y_n:]) #[-y_n:]
for i in range(len(predict)):print(round(predict[i],2))

#f.close()