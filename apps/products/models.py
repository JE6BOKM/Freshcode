from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "categories"


class Menu(models.Model):
    BADGE_CHOICES = [("NEW", "NEW"), ("BEST", "BEST")]
    name = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    isSold = models.BooleanField(default=False)
    badge = models.CharField(max_length=5, choices=BADGE_CHOICES, default="NEW")
    category = models.ForeignKey(
        "Category",
        related_name="menus",
        on_delete=models.CASCADE,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "menus"


class Tag(models.Model):
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    menuId = models.ForeignKey(
        Menu,
        related_name="tags",
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return self.name

    class Meta:
        db_table = "tags"


class Item(models.Model):
    SIZE_CHOICES = [("M", "M"), ("L", "L")]
    menuId = models.ForeignKey(
        Menu,
        related_name="items",
        on_delete=models.CASCADE,
    )
    name = models.CharField(max_length=50)
    size = models.CharField(max_length=5, choices=SIZE_CHOICES)
    price = models.IntegerField()
    isSold = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        db_table = "items"
