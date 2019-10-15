from django import forms

class AddressForm (forms.Form):
    latitude = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'latitude eg. 123.456789', 'id':'latitude'}),label='Latitude')
    longitude = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'longitude eg. 123.456789', 'id':'longitude'}),label='Longitude')
    radius = forms.DecimalField(widget=forms.NumberInput(attrs={'class':'form-control', 'placeholder':'radius(in km) eg. 123', 'id':'radius'} ))