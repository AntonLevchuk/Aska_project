from tkinter import Widget
from .models import Application

from django.forms import ModelForm, TextInput
from django import forms

class ApplicationForm(ModelForm):

    # nickname = forms.CharField(max_length=20)
    # ds_name = forms.CharField(max_length=40)
    # edit_link = forms.CharField(max_length=150)
    # other_links = forms.CharField(max_length=150)


    class Meta:
        model = Application
        fields = ['nickname', 'ds_name', 'edit_link', 'other_links']

        widgets = {
            'nickname': TextInput(attrs={
                'class': 'form__input nickname',
                'placeholder': 'Nickname',
            }),

            'ds_name': TextInput(attrs={
                'class': 'form__input ds-name',
                'placeholder': 'Discord name (example#1234)',
            }),

            'edit_link': TextInput(attrs={
                'class': 'form__input edit-link',
                'placeholder': 'Edit link',
            }),

            'other_links': TextInput(attrs={
                'class': 'form__input contacts',
                'placeholder': 'Contacts (IG or others)',
            }),
        }