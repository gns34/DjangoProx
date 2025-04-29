from django import form

class getCity(forms.Form):
    cityName=forms.CharField(
        label='Enter a city',
        max_length=50,
        widget=forms.TextInput(attrs={
            'placeholder' :'London, Amsterdam',
            'class':'form-control' 
        })

    )