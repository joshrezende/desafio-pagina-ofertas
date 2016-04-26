from django.contrib import admin
import nested_admin

from .models import Product, ProductImage, Offers, OffersOrigins

# Register your models here.
class ProductImageInline(nested_admin.NestedStackedInline):
    model = ProductImage
    extra = 5

class ProductOffersInline(nested_admin.NestedStackedInline):
    model = Offers
    extra = 2

class ProductAdmin(admin.ModelAdmin):
    fields = ['original_id', 'title', 'location', 'description']
    inlines = [ProductOffersInline, ProductImageInline]

admin.site.register(Product, ProductAdmin)
# admin.site.register(Offers)
