"""TitanicPj URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path

import TitanicApp.views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TitanicApp.views.index1, name='index1'),
    path('index1/', TitanicApp.views.index2, name='index2'),
    path('index1/index2', TitanicApp.views.index3, name='index3'),
    path('test1/', TitanicApp.views.test1, name='test1'),
    path('test1/add', TitanicApp.views.add, name='test1'),
    
]
