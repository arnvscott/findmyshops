from django import forms

class AddressForm (forms.Form):
    latitude = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'latitude eg. 123.456789', 'id':'latitude'}),label='Latitude', max_length=20)
    longitude = forms.CharField(widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'longitude eg. 123.456789', 'id':'longitude'}),label='Longitude', max_length=20)
