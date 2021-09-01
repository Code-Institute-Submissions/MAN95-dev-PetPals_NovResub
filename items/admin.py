from django.contrib import admin
from .models import Item, Type

# Register your models here.

class ItemAdmin(admin.ModelAdmin):
    list_display = (
        'name',
        'type',
        'price',
        'image',
    )

class TypeAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Item, ItemAdmin)
admin.site.register(Type, TypeAdmin)