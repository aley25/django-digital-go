from django.shortcuts import render
from django.http import HttpResponse
from .models import Feature
# Create your views here.
# request -> response
# request handler
# action

def index(request):
    
    feature1 = Feature.objects.all().first
    return render(request, 'index.html', {'feature': feature1})

def calculate():
    x = 1 
    y = 2
    return x

def say_hello(request):
    #pull data from db
    #Transform
    #send emails

    #returning templates, often not used with django
    x = calculate()
    return render(request, 'hello.html', {'name': 'Mosh'})

def word_counter(request):
        return render(request, 'counter.html')

def result(request):
    num = len(request.POST['text'])
    return render(request, 'result.html', { 'name': num })
