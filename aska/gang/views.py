from multiprocessing import context
from turtle import title
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Aska', 
    }
    return render(request, 'index.html', context)
