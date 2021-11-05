from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.products.models import Category, Item, Menu, Tag
from apps.products.serializers import (
    CategorySerializer,
    ItemSerializer,
    MenuSerializer,
    TagSerializer,
)
from apps.users.permissions import IsAdmin


class CategoryCRUDViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer

    # def get_permissions(self):
    #     if self.action in ["list", "retrieve"]:
    #         self.permission_classes = [AllowAny]
    #     else:
    #         self.permission_classes = [IsAdmin]
    #     return super().get_permissions()

    def get_permissions(self):
        if self.action in ["list"]:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()


class MenuCRUDViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()


class TagCRUDViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()


class ItemCRUDViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer

    def get_permissions(self):
        if self.action in ["list", "retrieve"]:
            self.permission_classes = [AllowAny]
        else:
            self.permission_classes = [IsAdmin]
        return super().get_permissions()
