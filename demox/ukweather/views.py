from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.
def index(request):
    return HttpResponse("Hello World")
def ukweather(request):
    template=loader.get_template('homefile.html')
    return HttpResponse(template.render())