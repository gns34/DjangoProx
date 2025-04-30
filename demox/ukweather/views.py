from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import *
from django.template import loader
from .forms import NameForm
import requests
from django.conf import settings
# Create your views here.
def index(request):
    return HttpResponse("Hello World")
# def ukweather(request):
#     template=loader.get_template('homefile.html')
#     return HttpResponse(template.render())

def ukweather(request):
    name = None
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
    else:
        form = NameForm()
    return render(request, 'homefile.html', {'form': form, 'name': name})
