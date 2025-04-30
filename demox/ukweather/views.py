from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import *
from django.template import loader
from .forms import CityName
import requests
from django.conf import settings
# Create your views here.
def index(request):
    return HttpResponse("Hello World")
# def ukweather(request):
#     template=loader.get_template('homefile.html')
#     return HttpResponse(template.render())

def ukweather(request):
    city = None
    if request.method == 'POST':
        form = CityName(request.POST)
        if form.is_valid():
            city = form.cleaned_data['city']
    else:
        form = CityName()
    return render(request, 'homefile.html', {'form': form, 'city': city})
