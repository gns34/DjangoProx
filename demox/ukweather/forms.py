from django import forms

class CityName(forms.Form):
    city = forms.CharField(label='Enter your city', max_length=100)
