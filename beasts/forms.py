from django.forms import ModelForm
from .models import Beast

class BeastForm(ModelForm):
    class Meta: 
        model = Beast
        fields = '__all__'