from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'hello.html',{'name':'vandit'})

def add(request):
    a = int(request.POST['num1'])
    b = int(request.POST['num2'])
 
    res = a + b 

    return render(request,'result.html',{'result':res})       