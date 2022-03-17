from json import detect_encoding
from django.shortcuts import render
from .forms import BeastForm
from django.http import HttpResponseRedirect
from .models import Beast

def entry(request):
    if request.method == 'POST':
        form = BeastForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") 
    else:
        form = BeastForm()
        query = Beast.objects.all().order_by('-create_date')
    return render(request, "entry.html", {
        "form": form,
        "query": query
    })