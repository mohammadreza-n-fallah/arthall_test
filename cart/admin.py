from django.contrib import admin
from .models import *


class ProductAdmin(admin.ModelAdmin):
    list_display = ("name",)
    search_fields = ("name",)
# Register your models here.
admin.site.register(Category)
admin.site.register(Product,ProductAdmin)
admin.site.register(Factor)