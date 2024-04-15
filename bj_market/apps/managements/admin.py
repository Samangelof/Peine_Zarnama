from django.contrib import admin
from django.contrib import admin
from .models import Product, Category, ProductImage


class ProductInline(admin.TabularInline):
    model = Product
    extra = 1

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    inlines = (ProductInline,)

admin.site.register(Product)

@admin.register(ProductImage)
class ProductImageAdmin(admin.ModelAdmin):
    pass
