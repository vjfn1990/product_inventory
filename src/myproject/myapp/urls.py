from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('sample_filling', views.sample_filling, name = 'sample_filling'),
    path('register', views.register, name = 'register'),
    path('retrieve_from_sku', views.retrieve_from_sku, name = 'retrieve_from_sku'),
    path('retrieve_available', views.retrieve_available, name = 'retrieve_available'),
    path('retrieve_sold_out', views.retrieve_sold_out, name = 'retrieve_sold_out')
]
