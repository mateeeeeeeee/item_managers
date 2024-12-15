from django.core.management.base import BaseCommand, CommandError
from shop.models import Category, Item,  Tag

class Command(BaseCommand):
    def handle(self, *args, **kwargs):

        Category.categoryobjects.with_item_count()

        Item.itemobject.with_tag_count()

        Tag.tagobjects.popular_tags(10)
        

        