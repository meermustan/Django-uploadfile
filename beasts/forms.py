
from dataclasses import fields
from django.forms import ModelForm
from django import forms
from .models import Beast

class BeastForm(ModelForm):
    
    class Meta:
        model = Beast
        fields = ('media',)
       
    
