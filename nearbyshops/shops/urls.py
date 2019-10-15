from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('getaddress/', views.getaddress, name='getaddress'),
]