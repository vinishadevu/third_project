from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse

def virat(request):
    return HttpResponse('<h1>virat is best batsman</h1>')