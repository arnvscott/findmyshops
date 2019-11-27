from django.shortcuts import render
from django.http import HttpResponseRedirect

from shops.models import Shop
from shops.forms import ChangeOriginForm, CurrentLocationForm


from django.contrib.gis.geos import GEOSGeometry
from django.contrib.gis.db.models.functions import Distance
from django.contrib.gis.measure import D # ``D`` is a shortcut for ``Distance``

# Create your views here.

def index(request):
        context = {}
        shops_list = []
        originform = ChangeOriginForm()
        locationform = CurrentLocationForm()
        context = {'shops' : shops_list, 'origin_form' : originform, 'location_form': locationform}
        return render(request, 'shops/index.html', context)

def changeorigin(request):
        context = {}
        shops_list = []
        form = ChangeOriginForm(request.GET)
        if form.is_valid():
                latitude = form.cleaned_data['latitude']
                longitude = form.cleaned_data['longitude']
                radius = form.cleaned_data['radius']
                pnt = GEOSGeometry(f'POINT({latitude} {longitude} )', srid=4326)
                if not radius:
                        shops_list = Shop.objects.annotate(distance=Distance('location',pnt)).order_by('distance')
                else:
                        shops_list = Shop.objects.filter(location__distance_lte=(pnt, D(km=radius))).annotate(distance=Distance('location',pnt)).order_by('distance')
                context = {'shops' : shops_list, 'form' : form}
        return render(request, 'shops/index.html', context)

def getlocations(request):
        context = {}
        locations = []
        target_list = []
        radius = 10
        originform = ChangeOriginForm()
        locationform = CurrentLocationForm()
        form = CurrentLocationForm(request.GET)
        if form.is_valid():
                latitude = form.cleaned_data['latitude']
                longitude = form.cleaned_data['longitude']
                pnt = GEOSGeometry(f'POINT({latitude} {longitude} )', srid=4326)
                locations = Shop.objects.filter(location__distance_lte=(pnt, D(km=radius))).annotate(distance=Distance('location',pnt)).order_by('distance')
                target_list = [{'name':site.name,'lat':site.location.x, 'lng':site.location.y} for site in locations]
                print (target_list)
        
        context = {'locations':target_list, 'origin_form':originform, 'location_form':locationform}
        return render(request, 'shops/locations.html', context)


 