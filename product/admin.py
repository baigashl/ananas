from django.contrib import admin
from .models import Product, Category, Cart

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Cart)
