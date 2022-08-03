from cProfile import run
from contextlib import redirect_stderr
from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import Test

#test

import numpy as np 
import pandas as pd 
import matplotlib.pyplot as plt

# 머신러닝

from sklearn.linear_model import LogisticRegression

import warnings
warnings.filterwarnings('ignore')

import pymysql as sql



# Create your views here.

def index1(request):
    return render(request, 'TitanicApp/index1.html')

def index2(request):
    return render(request, 'TitanicApp/index2.html')

def index2_2(request):
    
    return render(request, 'TitanicApp/index2_2.html')

def index3(request):
    
    conn = sql.connect(host='localhost',port=3306 ,user='Spaceship',password='Spaceship',db='spaceship')

    sql_1 = "select * from train"
    sql_2 = "select * from test"

    df_train = pd.read_sql_query(sql_1, conn)
    df_test = pd.read_sql_query(sql_2, conn)

    X_train = df_train.drop('Transported', axis=1)
    Y_train = df_train['Transported']

    X_test = df_test.drop('PassengerId', axis=1).copy()
    X_train.shape, Y_train.shape, X_test.shape
   
    #Logistic Regression
    logi_R = LogisticRegression()
    logi_R.fit(X_train, Y_train)
    Y_pre=logi_R.predict(X_test)
    acc_log = round(logi_R.score(X_train, Y_train)*100, 2)
    print(acc_log)

    output= pd.DataFrame(df_test)
    output['Transported'] = Y_pre
    print(output.tail())

    return render(request, 'TitanicApp/index3.html')

def test1(request):
    
    return render(request, 'TitanicApp/test1.html')

def add(request):
    test = Test()
    
    test.passengerid = request.POST['PassengerId']
    test.age = request.POST['Age']
    test.homeplanet = request.POST['HomePlanet']
    test.destination = request.POST['Destination']
    test.cryosleep = request.POST['CryoSleep']
    test.vip = request.POST['VIP']
    test.roomservice = request.POST['RoomService']
    test.foodcourt = request.POST['FoodCourt']
    test.shoppingmall = request.POST['ShoppingMall']
    test.spa = request.POST['Spa']
    test.vrdeck = request.POST['VRDeck']
    test.save()
   

    return HttpResponseRedirect('/index2_2')

def test2(request):
    
    conn = sql.connect(host='localhost',port=3306 ,user='Spaceship',password='Spaceship',db='spaceship')

    sql_1 = "select * from train"
    sql_2 = "select * from test"

    df_train = pd.read_sql_query(sql_1, conn)
    df_test = pd.read_sql_query(sql_2, conn)

    X_train = df_train.drop('Transported', axis=1)
    Y_train = df_train['Transported']

    X_test = df_test.drop('PassengerId', axis=1).copy()
    X_train.shape, Y_train.shape, X_test.shape
   
    #Logistic Regression
    logi_R = LogisticRegression()
    logi_R.fit(X_train, Y_train)
    Y_pre=logi_R.predict(X_test)
    acc_log = round(logi_R.score(X_train, Y_train)*100, 2)
    # print(acc_log)

    output= pd.DataFrame(df_test)
    output['Transported'] = Y_pre
    # print(output.infer_objects())
    # qs = output.infer_objects()
    
    # qs = Test.objects.filter(passengerid__startswith="최").values()
    # print(qs)
  
    last_output = pd.DataFrame(output.iloc[-1])
    
    context = {'last_output' : last_output.to_html()}
    
    return render(request, 'TitanicApp/test2.html', context)