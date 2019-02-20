from django.contrib import admin
from .models import Category, Product, ProductAlbum

# Register your models here.
admin.site.register(Category)
#admin.site.register(Product)

class ProductAblumInline(admin.StackedInline):
    model = ProductAlbum
    max_num = 10


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAblumInline]