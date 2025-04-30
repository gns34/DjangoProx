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

# def ukweather(request):
#     city = None
#     if request.method == 'POST':
#         form = CityName(request.POST)
#         if form.is_valid():
#             city = form.cleaned_data['city']
#     else:
#         form = CityName()
#     return render(request, 'homefile.html', {'form': form, 'city': city})

def ukweather(request):
    api_key = "0c9c60916923359f99d5340e35482f4f" 
    city = request.GET.get('city', 'London')  # Get city from user input, default to Nairobi
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    response = requests.get(url)
    data = response.json()
    print(data)
    if response.status_code == 200:
        context = {
            'city': city,
            'temp': data['main']['temp'],
            'humidity': data['main']['humidity'],
            'description': data['weather'][0]['description'],
        }
    else:
        context = {'error': 'City not found. Please try again.'}

    return render(request, 'homefile.html', context)
