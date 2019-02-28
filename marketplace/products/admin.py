from django.contrib import admin
from .models import Product, Category, ProductAlbum, Stock, Comment

# Register your models here.
admin.site.register(Category)
#admin.site.register(Product)

class ProductAblumInline(admin.StackedInline):
    model = ProductAlbum
    max_num = 10

class StockInline(admin.StackedInline):
    model = Stock
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductAblumInline, StockInline]

