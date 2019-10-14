from django.shortcuts import render

from shops.models import Shop
# Create your views here.

def index(request):
        context = {}
        shops_list = Shop.objects.all()
        context = {'shops' : shops_list}
        return render(request, 'shops/index.html', context)