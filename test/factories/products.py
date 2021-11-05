import factory
import factory.fuzzy
from factory.django import DjangoModelFactory
from faker import Faker

from apps.products.models import Category, Item, Menu, Tag

__all__ = ["CateGoryFactory", "MenuFactory", "TagFactory", "ItemFactory"]

fake = Faker()


class CateGoryFactory(DjangoModelFactory):
    name = factory.Faker("word")
    menus = factory.RelatedFactoryList(
        "test.factories.MenuFactory", factory_related_name="category", size=5
    )

    class Meta:
        model = Category
        django_get_or_create = ["name"]


class MenuFactory(DjangoModelFactory):
    name = factory.Faker("word")
    description = factory.Faker("text")
    isSold = factory.Faker("boolean")
    badge = factory.Faker("random_element", elements=["NEW", "BEST"])
    category = factory.SubFactory(CateGoryFactory)
    tags = factory.RelatedFactoryList(
        "test.factories.TagFactory", factory_related_name="menuId", size=5
    )
    items = factory.RelatedFactoryList(
        "test.factories.ItemFactory", factory_related_name="menuId", size=5
    )

    class Meta:
        model = Menu
        django_get_or_create = ["name"]


class TagFactory(DjangoModelFactory):
    type = factory.Faker("word")
    name = factory.Faker("word")
    menuId = factory.SubFactory(MenuFactory)

    class Meta:
        model = Tag
        django_get_or_create = ["name"]


class ItemFactory(DjangoModelFactory):
    menuId = factory.SubFactory(MenuFactory)
    name = factory.Faker("word")
    size = factory.Faker("random_element", elements=["M", "L"])
    price = factory.fuzzy.FuzzyInteger(100, 1000000)
    isSold = factory.Faker("boolean")

    class Meta:
        model = Item
        django_get_or_create = ["name"]
