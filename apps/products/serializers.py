from rest_framework import serializers

from apps.products.models import Menu, Tag, Item


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"


class MenuSeiralier(serializers.ModelSerializer):
    items = ItemSerializer(many=True, read_only=True)
    tags = TagSerializer(many=True, read_only=True)

    class Meta:
        model = Menu
        fields = (
            "name",
            "description",
            "isSold",
            "badge",
            "category",
            "items",
            "tags",
        )
