import json
from django.core import serializers
from django.http import HttpResponse
from myapp.models import Product

def process_products(model_object):
    raw_products = json.loads(serializers.serialize('json', model_object))
    processed_products = []
    for raw_product in raw_products:
        processed_products.append({'sku': raw_product['fields']['sku'], 'name': raw_product['fields']['name'], 'qty': raw_product['fields']['qty'], 'price': raw_product['fields']['price']})
    return json.dumps(processed_products)

def index(request):
    return HttpResponse(json.dumps([]), content_type = 'application/json')

def sample_filling(request):
    p = Product(sku = 'A0B1C2D3', name = 'Bread', qty = 8, price = 3.4)
    p.save()
    p = Product(sku = 'B0C1D2E3', name = 'Eggs', qty = 4, price = 2.1)
    p.save()
    p = Product(sku = 'C0D1E2F3', name = 'Milk', qty = 6, price = 5.2)
    p.save()
    p = Product(sku = 'D0E1F2G3', name = 'Cheese', qty = 0, price = 9.9)
    p.save()
    p = Product(sku = 'E0F1G2H3', name = 'Rice', qty = 2, price = 7.5)
    p.save()
    p = Product(sku = 'F0G1H2I3', name = 'Pasta', qty = 7, price = 8.0)
    p.save()
    p = Product(sku = 'G0H1I2J3', name = 'Sugar', qty = 0, price = 0.1)
    p.save()
    p = Product(sku = 'H0I1J2K3', name = 'Salt', qty = 5, price = 1.7)
    p.save()
    return HttpResponse(process_products(Product.objects.all()), content_type = 'application/json')

def register(request):
    sku = request.GET.get('sku', 'None')
    name = request.GET.get('name', 'None')
    qty = request.GET.get('qty', 'None')
    price = request.GET.get('price', 'None')
    p = Product(sku = sku, name = name, qty = qty, price = price)
    p.save()
    processed_p = {'sku': sku, 'name': name, 'qty': qty, 'price': price}
    return HttpResponse(json.dumps(processed_p), content_type = 'application/json')

def retrieve_from_sku(request):
    sku = request.GET.get('sku', 'None')
    raw_p = json.loads(serializers.serialize('json', Product.objects.filter(sku = sku)))
    processed_p = {'sku': raw_p[0]['fields']['sku'], 'name': raw_p[0]['fields']['name'], 'qty': raw_p[0]['fields']['qty'], 'price': raw_p[0]['fields']['price']}
    return HttpResponse(json.dumps(processed_p), content_type = 'application/json')

def retrieve_available(request):
    return HttpResponse(process_products(Product.objects.filter(qty__gte = 1)), content_type = 'application/json')

def retrieve_sold_out(request):
    return HttpResponse(process_products(Product.objects.filter(qty__lte = 0)), content_type = 'application/json')
