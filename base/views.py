import re
from django.shortcuts import render
from django.http import HttpResponse

def home(request):
    return render(request,'home.html')
def nextpage(request):
    return render(request,'nextpage.html')
