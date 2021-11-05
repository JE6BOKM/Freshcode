from rest_framework import viewsets
from rest_framework.permissions import AllowAny

from apps.products.models import Category, Menu, Tag, Item
from apps.products.serializers import CategorySerializer, MenuSerializer, TagSerializer, ItemSerializer

class CategoryCRUDViewSet(viewsets.ModelViewSet):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    permission_classes = [AllowAny]

class MenuCRUDViewSet(viewsets.ModelViewSet):
    queryset = Menu.objects.all()
    serializer_class = MenuSerializer
    permission_classes = [AllowAny]

class TagCRUDViewSet(viewsets.ModelViewSet):
    queryset = Tag.objects.all()
    serializer_class = TagSerializer
    permission_classes = [AllowAny]

class ItemCRUDViewSet(viewsets.ModelViewSet):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer
    permission_classes = [AllowAny]