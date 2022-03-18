from json import detect_encoding
from django.shortcuts import render
from .forms import BeastForm
from django.http import HttpResponseRedirect
from .models import Beast

def entry(request):
    if request.method == 'POST':
        for item in request.FILES.getlist('media'):
            Beast.objects.update_or_create(media=item)
        return HttpResponseRedirect("/") 
    else:
        query = Beast.objects.all().order_by('-create_date')
        return render(request, "entry.html", {
            "query": query
        })