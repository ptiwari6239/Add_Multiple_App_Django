from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    return render(request,'Home.html',{'name':'ptiwari'})
def add(request):
    val1 = int(request.POST["nu1"])
    val2 = int(request.POST["nu2"])
    res = val1+val2
    return render(request,'result.html',{'result':res})    
def multiple(request):
    va1 = int(request.POST["num1"])
    va2 = int(request.POST["num2"])   
    rest = va1*va2 
    return render(request,'res.html',{'resul':rest})