from django.conf import settings
from django.core.cache import cache

from catalog.models import Category


def get_cached_categories():
    if settings.CACHE_ENABLED:
        category_list = cache.get('category')
        if category_list is None:
            category_list = Category.objects.all()
            cache.set('category', category_list)
            return category_list
        else:
            return category_list