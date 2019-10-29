from django import forms

class AddressForm (forms.Form):
    latitude = forms.DecimalField(label='Latitude')
    longitude = forms.DecimalField(label='Longitude')
    radius = forms.DecimalField(label='Radius')