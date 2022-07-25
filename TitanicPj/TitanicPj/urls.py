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
    path('', TitanicApp.views.Main, name='Main'),
    path('Main/', TitanicApp.views.Questions1, name='Questions1'),
    path('Main/Questions1/', TitanicApp.views.Questions2, name='Questions2'),
    path('Main/Questions1/Questions2', TitanicApp.views.Questions3, name='Questions3'),
    path('Main/Questions1/Questions2/Questions3', TitanicApp.views.Questions4, name='Questions4'),
    path('', TitanicApp.views.Questions5, name='Questions5'),
    path('', TitanicApp.views.Questions6, name='Questions6'),
    path('', TitanicApp.views.Questions7, name='Questions7'),
    path('', TitanicApp.views.Questions8, name='Questions8'),
    path('', TitanicApp.views.Questions9, name='Questions9'),
    path('', TitanicApp.views.Questions10, name='Questions10'),
    path('', TitanicApp.views.Questions11, name='Questions11'),
    path('', TitanicApp.views.Questions12, name='Questions12'),
    path('', TitanicApp.views.Questions13, name='Questions13'),

    
]
