from django.core.management import BaseCommand

from catalog.models import Category, Product


class Command(BaseCommand):

    # def handle(self, *args, **options):
    #     category_list = [
    #         {'name': 'Овощи', 'desc': 'Описание категории овощи'},
    #         {'name': 'Фрукты', 'desc': 'Описание категории фрукты'},
    #         {'name': 'Бытовая химия', 'desc': 'Описание категории бытовая химия'}
    #     ]
    #     category_for_create = []
    #     for item in category_list:
    #         category_for_create.append(Category(**item))
    #     Category.objects.all().delete()
    #     Category.objects.bulk_create(category_for_create)

    def handle(self, *args, **options):
        product_list = [
            {'name': 'Помидор', 'desc': 'Описание помидорки', 'cat': 'Category.Овощи', 'price': '30'},
            {'name': 'Арбуз', 'desc': 'Описание арбуза', 'cat': '2', 'Category.Фрукты': '60'}
        ]
        product_for_create = []
        for item in product_list:
            product_for_create.append(Product(**item))
        Product.objects.all().delete()
        Product.objects.bulk_create(product_for_create)
