from django import forms

class AddressForm (forms.Form):
    latitude = forms.DecimalField(label='Latitude', required=False, widget=forms.NumberInput(attrs={'class':'full-width','placeholder':'latitude eg. 123.456789'}))
    longitude = forms.DecimalField(label='Longitude', required=False, widget=forms.NumberInput(attrs={'class':'full-width','placeholder':'longitude eg. 123.456789'}))
    radius = forms.DecimalField(label='Radius', required=False, widget=forms.NumberInput(attrs={'class':'full-width','placeholder':'range eg. 3'}))