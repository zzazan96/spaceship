from contextlib import redirect_stderr
from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'TitanicApp/index.html')