from django.contrib import admin
from apps.products.models import Category, Menu, Item, Tag


@admin.register(Menu)
class MenuAdmin(admin.ModelAdmin):

    """Menu Admin Definition"""


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):

    """Tag Admin Definition"""


@admin.register(Item)
class ItemAdmin(admin.ModelAdmin):

    """Item Admin Definition"""


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):

    """Category Admin Definition"""
