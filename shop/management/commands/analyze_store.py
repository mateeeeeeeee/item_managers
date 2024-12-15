from django.db.models import Sum,Max,Min,Avg,Count
from django.core.management.base import BaseCommand, CommandError
from shop.models import Category, Item,  Tag


class Command(BaseCommand):
    def handle(self, *args, **kwargs):
# aggregate
        # category_name = "Food staff"
        # categories = Category.objects.filter(name=category_name).aggregate(item_count=Count('items'))
        # print(categories)

        # all_products = Item.objects.aggregate(
        #     max = Max('price'),
        #     min = Min('price'),
        #     avg = Avg('price')
        # )
        # print(all_products)

# annotete
        # categories = Category.objects.annotate(items_count=Count('items'))
        # for item in categories:
        #     print(item.name,item.items_count)

        # categories = Category.objects.annotate(sum=Sum('items__price',default=0))
        # for item in categories:
        #     print(item.sum)

# select_related
        # items = Item.objects.select_related('category').all()
        # print(items)

        # items = Item.objects.select_related('category').all()
        # for i in items:
        #     print(i.name)

# prefetch_related
        items = Item.objects.prefetch_related('tags').all()
        for item in items:
            for tag in item.tags.all():
                print(f'{item.name}: {tag.name}')
                







