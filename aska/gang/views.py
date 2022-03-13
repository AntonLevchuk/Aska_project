from email.mime import application
from multiprocessing import context
from turtle import title
from django.shortcuts import redirect, render

from .models import Member, Application
from .forms import ApplicationForm

def index(request):
    context = {
        'title': 'Aska', 
    }
    return render(request, 'index.html', context)


def members(request):
    member = Member.objects.order_by('id')
    context = {
        'member': member,
        'title': 'Members',
    }
    return render(request, 'members.html', context)


def join_us(request):
    error = ''
    if request.method == 'POST':
        form = ApplicationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Incorrect form'

    form = ApplicationForm()

    context = {
        'title': 'Application form',
        'form': form,
        'error': error,
    }
    return render(request, 'join_us.html', context)


