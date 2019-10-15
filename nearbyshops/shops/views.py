from django.shortcuts import render

from shops.models import Shop
from shops.forms import AddressForm
# Create your views here.

def index(request):
        context = {}
        shops_list = Shop.objects.all()
        addressform = AddressForm()
        context = {'shops' : shops_list, 'form' : addressform}
        return render(request, 'shops/index.html', context)