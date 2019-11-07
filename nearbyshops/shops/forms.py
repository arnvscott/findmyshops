from django import forms

class AddressForm (forms.Form):
    latitude = forms.DecimalField(label='Latitude', widget=forms.NumberInput(attrs={'class':'full-width','placeholder':'latitude eg. 123.456789'}))
    longitude = forms.DecimalField(label='Longitude', widget=forms.NumberInput(attrs={'class':'full-width','placeholder':'longitude eg. 123.456789'}))
    radius = forms.DecimalField(label='Radius', widget=forms.NumberInput(attrs={'class':'full-width','placeholder':'range eg. 3'}))