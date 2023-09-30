from django.urls import path
from django.contrib import admin

from blog.apps import BlogConfig
from blog.views import BlogMaterialCreateView, BlogMaterialListView, BlogMaterialDetailView, BlogMaterialUpdateView, \
    BlogMaterialDeleteView
from config import settings
from django.conf.urls.static import static


app_name = BlogConfig.name
urlpatterns = [
    path('admin/', admin.site.urls),
    path('create/', BlogMaterialCreateView.as_view(), name='create'),
    path('', BlogMaterialListView.as_view(), name='list'),
    path('view/<slug:slug>/', BlogMaterialDetailView.as_view(), name='view'),
    path('update/<int:pk>/', BlogMaterialUpdateView.as_view(), name='update'),
    path('delete/<int:pk>/', BlogMaterialDeleteView.as_view(), name='delete')
    ]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)