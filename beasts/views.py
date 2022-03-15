from django.shortcuts import render
from .forms import BeastForm
from django.http import HttpResponseRedirect

def entry(request):
    if request.method == 'POST':
        form = BeastForm(request.POST, request.FILES)
        
        if form.is_valid():
            form.save()
            return HttpResponseRedirect("/") 
    else:
        form = BeastForm()

    return render(request, "entry.html", {
        "form": form
    })