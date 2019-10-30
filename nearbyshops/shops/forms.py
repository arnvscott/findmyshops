from django import forms

class AddressForm (forms.Form):
    latitude = forms.DecimalField(label='Latitude', widget=forms.NumberInput(attrs={'class':'wide_input'}))
    longitude = forms.DecimalField(label='Longitude', widget=forms.NumberInput(attrs={'class':'wide_input'}))
    radius = forms.DecimalField(label='Radius', widget=forms.NumberInput(attrs={'class':'wide_input'}))