from django.db import models
from django.db.models.deletion import CASCADE

class Category(models.Model):
    name = models.CharField(max_length=16)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'categories'

class Menu(models.Model):
    BADGE_CHOICES = [
        ('NEW', 'NEW'),
        ('BEST', 'BEST')
    ]
    name        = models.CharField(max_length=32)
    description = models.CharField(max_length=512)
    isSord      = models.BooleanField(default=False)
    badge       = models.CharField(max_length=5, choices=BADGE_CHOICES)
    category    = models.ForeignKey('Category', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'menus'

class Tag(models.Model):
    type = models.CharField(max_length=32)
    name = models.CharField(max_length=32)
    menu = models.ForeignKey('Menu', on_delete=models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'tags'

class Item(models.Model):
    SIZE_CHOICES = [
        ('M', 'M'),
        ('L', 'L')
    ]
    name   = models.CharField(max_length=50)
    size   = models.CharField(max_length=5, choices=SIZE_CHOICES)
    price  = models.IntegerField()
    isSold = models.BooleanField(default=False)
    menu   = models.ForeignKey('Menu', on_delete=CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'items'