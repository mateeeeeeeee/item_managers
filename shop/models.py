from django.db import models
from django.db.models import Count

class CategoryManager(models.Manager):
    def with_item_count(self):
        categories = self.annotate(item_count=Count('items'))
        for category in categories:
            print(f'{category.name}: {category.item_count}')

class ItemManager(models.Manager):
    def with_tag_count(self):
        items = self.annotate(tags_count = Count('tags'))
        for item in items:
            print(f'{item.name}: {item.tags_count}')

class TagManager(models.Manager):
    def popular_tags(self, min_items):
        tags = self.annotate(item_count=Count('items')).filter(item_count__gte=min_items)
        for tag in tags:
            print(f'{tag.name}')


class Category(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    categoryobjects = CategoryManager()

    def __str__(self):
        return self.name

class Item(models.Model):
    name = models.CharField(max_length=255)
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='items')
    price = models.DecimalField(max_digits=10, decimal_places=2)
    description = models.TextField(blank=True, null=True)
    itemobject = ItemManager()

    def __str__(self):
        return self.name

class Tag(models.Model):
    name = models.CharField(max_length=50)
    items = models.ManyToManyField(Item, related_name='tags', blank=True)
    tagobjects = TagManager()

    def __str__(self):
        return self.name
