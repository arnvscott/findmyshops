from django.shortcuts import render
from django.http import HttpResponseRedirect

from shops.models import Shop
from shops.forms import CurrentLocationForm

from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``
 
# Create your views here.

def index(request):
        context = {}
        shops_list = []
        locationform = CurrentLocationForm()
        context = {'shops' : shops_list, 'location_form': locationform}
        return render(request, 'shops/index.html', context)

def getlocations(request):
        context = {}
        locations = []
        target_list = []
        radius = 10
        locationform = CurrentLocationForm()
        form = CurrentLocationForm(request.GET)
        if form.is_valid():
                latitude = form.cleaned_data['latitude']
                longitude = form.cleaned_data['longitude']
                pnt = GEOSGeometry(f'POINT({latitude} {longitude} )', srid=4326)
                locations = Shop.objects.filter(location__distance_lte=(pnt, D(km=radius))).annotate(distance=Distance('location',pnt)).order_by('distance')
                target_list = [{'name':site.name,'lat':site.location.x, 'lng':site.location.y} for site in locations]
                print (target_list)
        
        context = {'locations':target_list, 'location_form':locationform}
        return render(request, 'shops/locations.html', context)


 