from .models import Application

from django.forms import ModelForm

class ApplicationForm(ModelForm):
    class Meta:
        model = Application
        fields = ['nickname', 'ds_name', 'edit_link', 'edit_link', 'other_links', 'result']