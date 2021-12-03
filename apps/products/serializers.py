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
    
    def update(self, instance, validated_data):
        items_data = validated_data.pop("items")
        tags_data = validated_data.pop("tags")
        
        # Maps for id->instance and id->data item.
        book_mapping = {book.id: book for book in instance}
        data_mapping = {item['id']: item for item in validated_data}

        # Perform creations and updates.
        ret = []
        for book_id, data in data_mapping.items():
            book = book_mapping.get(book_id, None)
            if book is None:
                ret.append(self.child.create(data))
            else:
                ret.append(self.child.update(book, data))

        # Perform deletions.
        for book_id, book in book_mapping.items():
            if book_id not in data_mapping:
                book.delete()

        return ret
