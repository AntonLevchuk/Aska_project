from django.urls import path
from gang.views import * 

urlpatterns = [
    path('', index, name='home')
]