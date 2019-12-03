from django import forms


class CurrentLocationForm (forms.Form):
    latitude = forms.DecimalField(label='Latitude', widget=forms.NumberInput(attrs={'class':'full-width', 'id':'cur_lat'}))
    longitude = forms.DecimalField(label='Longitude', widget=forms.NumberInput(attrs={'class':'full-width', 'id':'cur_lng'}))
