import numpy as np
import pandas as pd
from sklearn.linear_model import Ridge
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline
import matplotlib.pyplot as plt

f = open('office.txt','r')

#Read training dataset
F,N = map(int, f.readline().split())
featlist = []
for i in range (F):
    featlist.append('F'+str(i))
featlist.append('y')
df_train = pd.DataFrame(columns=featlist)
for i in range(N):
    a = [float(x) for x in f.readline().split()]
    df_train=df_train.append(dict(zip(featlist,a)),ignore_index=True)

#Read test dataset
y_n = int(f.readline())

for i in range(y_n):
    a = [float(x) for x in f.readline().split()]
    df_train = df_train.append(dict(zip(featlist[:F],a)),ignore_index=True)

result = make_pipeline(PolynomialFeatures(F), Ridge())
result.fit(df_train[featlist[:-1]][:-y_n],list(df_train['y'][:-y_n]))

predict=result.predict(df_train[featlist[:-1]][-y_n:]) #[-y_n:]
for i in range(len(predict)):print(round(predict[i],2))

f.close()