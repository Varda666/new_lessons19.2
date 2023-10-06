from django.urls import path
from django.contrib import admin

from catalog.views import ProductCreateView, ProductListView, ProductDetailView, ProductUpdateView, ProductDeleteView, \
    ContactCreateView
# from catalog.views import catalog_home, catalog_contacts, catalog_product, add_product
from config import settings
from django.conf.urls.static import static

app_name = 'catalog'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', ProductCreateView.as_view(), name='create_product'),
    path('', ProductListView.as_view(), name='list_product'),
    path('detail/<int:pk>/', ProductDetailView.as_view(), name='detail_product'),
    path('update/<int:pk>/', ProductUpdateView.as_view(), name='update_product'),
    path('delete/<int:pk>/', ProductDeleteView.as_view(), name='delete_product'),
    path('create/contact/', ContactCreateView.as_view(), name='create_contact')
]

# urlpatterns = [
#     path('admin/', admin.site.urls),
#     path('', catalog_home, name='home'),
#     path('contacts/', catalog_contacts, name='contacts'),
#     # path('info/', catalog_contacts, name='catalog_contacts_post'),
#     path('catalog/<int:pk>/', catalog_product, name='catalog_product'),
#     path('product_add/', add_product, name='add_product')
# ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)