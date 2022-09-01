from cgitb import reset
from multiprocessing import context
from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request, 'index.html')

def greeting(request):
    foods = ['apple', 'banana', 'coconut',]
    return render(request, 'greeting.html', foods)

def throw(request):
    return render(request, 'throw.html')

def catch(request):
    message = request.GET.get('message')
    print("message= ", message)
    context = {
        'message' : message,
    }
    return render(request, 'catch.html', context)

def hello(request, name):
    context = {
        'name' : name,
    }
    return render(request, 'hello.html', context)