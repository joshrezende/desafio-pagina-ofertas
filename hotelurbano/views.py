from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse

from pprint import pprint

from .models import Product, ProductImage, Offers, OffersOrigins

# Create your views here.
def index(request):
    products_list = Product.objects.all()
    context = {'products':products_list}
    return render(request, 'index.html', context)

def product(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    images = product.images.all()
    offers = product.offers.all()

    context = {
        'product': product,
        'images': images,
        'offers': offers
    }
    return render(request, 'product.html', context)
