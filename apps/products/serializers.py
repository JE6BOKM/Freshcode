from rest_framework import serializers

from apps.products.models import Category, Item, Menu, Tag

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = '__all__'

class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = '__all__'

class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = '__all__'

class MenuSerializer(serializers.ModelSerializer):
    categories = CategorySerializer(many=True, read_only=True)
    items = ItemSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = ["id", "categories", "name", "description", "isSold", "badge", "items", "tags"]

