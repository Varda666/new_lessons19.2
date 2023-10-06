from django.db import models
from django.urls import reverse


class BlogMaterial(models.Model):
    name = models.CharField(max_length=150, verbose_name='заголовок')
    slug = models.SlugField(max_length=150, allow_unicode=False, verbose_name='slug',)
    content = models.TextField(default='',verbose_name='содержимое')
    imd = models.ImageField(upload_to='media/', verbose_name='изображение')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    published = models.BooleanField(default=True, verbose_name='признак публикации')
    views_count = models.PositiveIntegerField(default=0, verbose_name='количество просмотров')


    def __str__(self):
        # Строковое отображение объекта
        return self.name, self.slug, self.imd

    def get_absolute_url(self):
        return reverse('blogmaterial_detail', kwargs={'slug': self.slug})

    class Meta:
        verbose_name = 'блог' # Настройка для наименования одного объекта
        verbose_name_plural = 'блоги' # Настройка для наименования набора объектов

# Create your models here.
