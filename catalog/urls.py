from django.urls import path
from django.contrib import admin

from catalog.views import catalog_home, catalog_contacts, catalog_product, add_product
from config import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', catalog_home, name='home'),
    path('contacts/', catalog_contacts, name='contacts'),
    # path('info/', catalog_contacts, name='catalog_contacts_post'),
    path('product/', catalog_product, name='catalog_product'),
    path('product_add/', add_product, name='add_product')
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)