import json
from pprint import pprint

from .models import Product, ProductImage, Offers, OffersOrigins

def insert_offers(product, item):
    original_id = item.get('id')
    product_key = product.id
    offer, created = Offers.objects.get_or_create(original_id=original_id, product_id=product_key)

    # pprint(original_id)

    offer.title = item.get('title')
    offer.description = item.get('description')
    offer.daily = item.get('daily')
    offer.price = item.get('price')

    offer.save()

def insert_product(item):
    original_id = item.get('id')
    product, created = Product.objects.get_or_create(original_id=original_id)

    product.title = item.get('title')
    product.location = item.get('location')
    product.description = item.get('description')

    for furfles in item.get('options'):
        # pprint(furfles)
        insert_offers(product, furfles)

    product.save()

    if created:
        pprint("criado")
    else:
        pprint("atualizado")

def furfles():
    with open('offers.json') as data_file:
        data = json.load(data_file)

    for item in data:
        insert_product(item)
