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

df_train = pd.read_sql_query(sql_1, conn)
df_train.head()
