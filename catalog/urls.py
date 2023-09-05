from django.urls import path

from catalog.views import catalog_home, catalog_contacts, catalog_contacts_post
app_name = 'catalog'

urlpatterns = [
    path('', catalog_home, name='home'),
    path('contacts/', catalog_contacts, name='contacts'),
    path('info/', catalog_contacts_post, name='catalog_contacts_post')
]