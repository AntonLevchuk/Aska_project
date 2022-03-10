from unicodedata import name
from django.urls import path
from gang.views import * 

urlpatterns = [
    path('', index, name='home'),
    path('members/', members, name='members'),
    path('join_us/', join_us, name='join_us'),
]