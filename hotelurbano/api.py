import json
from pprint import pprint
from django.core.files import File
from django.core.files.temp import NamedTemporaryFile

from .models import Product, ProductImage, Offers, OffersOrigins

def insert_offers(product, item):
    original_id = item.get('id')
    product_key = product.id
    offer, created = Offers.objects.get_or_create(original_id=original_id, product_id=product_key)

    offer.title = item.get('title')
    offer.description = item.get('description')
    offer.daily = item.get('daily')
    offer.price = item.get('price')

    for origin in item.get('from'):
        # pprint(origin)
        insert_origins(offer, origin)

    offer.save()

def insert_photos(product, item):
    photo = ProductImage()

    name = item.split('/')[-1]
    photo.product = product
    photo.image = File(open(item))

    photo.save()

def insert_origins(offer2, item):
    origin = OffersOrigins()
    origin.offer = offer2

    origin.origin_name = item

    origin.save()


def insert_product(item):
    original_id = item.get('id')
    product, created = Product.objects.get_or_create(original_id=original_id)

    product.title = item.get('title')
    product.location = item.get('location')
    product.description = item.get('description')

    for offer in item.get('options'):
        insert_offers(product, offer)

    for image in item.get('photos'):
        # pprint(image)
        insert_photos(product, image)

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
