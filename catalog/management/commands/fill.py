from django.core.management import BaseCommand

from catalog.models import Category


class Command(BaseCommand):

    def handle(self, *args, **options):
        category_list = [
            {'cat_name': 'Овощи', 'cat_desc': 'Описание категории овощи'},
            {'cat_name': 'Фрукты', 'cat_desc': 'Описание категории фрукты'},
            {'cat_name': 'Бытовая химия', 'cat_desc': 'Описание категории бытовая химия'}
        ]
        category_for_create = []
        for item in category_list:
            category_for_create.append(Category(**item))
        Category.objects.all().delete()
        Category.objects.bulk_create(category_for_create)

