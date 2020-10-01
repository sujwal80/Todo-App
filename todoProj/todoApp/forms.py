from django import forms
from django.forms import ModelForm
from .models import task

class task_form(ModelForm):

    class Meta:
        model = task
        fields = '__all__'
