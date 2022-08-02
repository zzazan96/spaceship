from contextlib import redirect_stderr
from django.shortcuts import render

from TitanicApp.models import Test

from django.http import HttpResponseRedirect


# Create your views here.

def index1(request):
    return render(request, 'TitanicApp/index1.html')

def index2(request):
    return render(request, 'TitanicApp/index2.html')

def index3(request):
    return render(request, 'TitanicApp/index3.html')

def test1(request):
    return render(request, 'TitanicApp/test1.html')

def add(request):
    test = Test()
    
    test.passengerid = request.POST['PassengerId']
    test.save()
   

    return HttpResponseRedirect('/Main')