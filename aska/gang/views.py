from email.mime import application
from multiprocessing import context
from turtle import title
from django.shortcuts import render

def index(request):
    context = {
        'title': 'Aska', 
    }
    return render(request, 'index.html', context)


def members(request):
    context = {
        'title': 'Members',
    }
    return render(request, 'members.html', context)


def join_us(request):
    context = {
        'title': 'Application form',
    }
    return render(request, 'join_us.html', context)
