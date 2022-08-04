import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# 머신러닝

from sklearn.linear_model import LogisticRegression
from sklearn.svm import SVC, LinearSVC
from sklearn.ensemble import RandomForestClassifier
from sklearn.neighbors import KNeighborsClassifier
from sklearn.naive_bayes import GaussianNB
from sklearn.linear_model import Perceptron
from sklearn.linear_model import SGDClassifier
from sklearn.tree import DecisionTreeClassifier




import warnings
warnings.filterwarnings('ignore')

import pymysql as sql

conn = sql.connect(host='localhost',port=3306 ,user='Spaceship',password='Spaceship',db='spaceship')



sql_1 = "select * from train"
sql_2 = "select * from test"

df_train = pd.read_sql_query(sql_1, conn)
df_test = pd.read_sql_query(sql_2, conn)
head=df_train.head()
# print(head)

X_train = df_train.drop('Transported', axis=1)
Y_train = df_train['Transported']

X_test = df_test.drop('PassengerId', axis=1).copy()
X_train.shape, Y_train.shape, X_test.shape

# print(X_train.shape)
# print(Y_train.shape)
# print(X_test.shape)

#Logistic Regression
logi_R = LogisticRegression()
logi_R.fit(X_train, Y_train)
Y_pre=logi_R.predict(X_test)
acc_log = round(logi_R.score(X_train, Y_train)*100, 2)
print(acc_log)

# output= pd.DataFrame({
#         "PassengerId": df_test["PassengerId"],
#         "Transported": Y_pre
#     })

output= pd.DataFrame(df_test)
output['Transported'] = Y_pre

mean_CS = output[["CryoSleep", "Transported"]].groupby(['CryoSleep'], as_index=True).mean()
mean_VIP =output[["VIP", "Transported"]].groupby(['VIP'], as_index=True).mean()
mean_HP =output[["HomePlanet", "Transported"]].groupby(['HomePlanet'], as_index=True).mean()
mean_DT =output[["Destination", "Transported"]].groupby(['Destination'], as_index=True).mean()
mean_AGE =output[["Age", "Transported"]].groupby(['Age'], as_index=True).mean()
# print(output.tail())
# print("action")
# train[train["Transported"] == 1]["Age"]

print(mean_CS)
print(mean_VIP)
print(mean_HP)
print(mean_DT)
print(mean_AGE)


    
# learning(conn)