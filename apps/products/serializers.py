from rest_framework import serializers

from apps.products.models import Item, Menu, Tag


class ItemSerializer(serializers.ModelSerializer):
    class Meta:
        model = Item
        fields = "__all__"
        read_only_fields = ["menuId"]


class TagSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tag
        fields = "__all__"
        read_only_fields = ["menuId"]


class MenuSerialier(serializers.ModelSerializer):
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


class CreateUpdateMenuSerialier(serializers.ModelSerializer):
    items = ItemSerializer(many=True)
    tags = TagSerializer(many=True)

    class Meta:
        model = Menu
        fields = (
            "name",
            "description",
            "isSold",
            "badge",
            "category",
            "tags",
            "items",
        )

    def create(self, validated_data):
        items_data = validated_data.pop("items")
        tags_data = validated_data.pop("tags")
        menu = Menu.objects.create(**validated_data)
        for item_data in items_data:
            Item.objects.create(menuId=menu, **item_data)
        for tag_data in tags_data:
            Tag.objects.create(menuId=menu, **tag_data)
        return menu
