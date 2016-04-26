from django.core.management.base import BaseCommand, CommandError
from hotelurbano.models import Product, ProductImage, Offers, OffersOrigins
from hotelurbano import api

class Command(BaseCommand):
    def handle(self, *args, **options):
        api.furfles()
