from django.db import models


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование')
    desc = models.TextField(verbose_name='описание')
    imd = models.ImageField(upload_to='media/', verbose_name='изображение')
    cat = models.ForeignKey('Category', on_delete=models.DO_NOTHING, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = 'товар' # Настройка для наименования одного объекта
        verbose_name_plural = 'товары' # Настройка для наименования набора объектов


class Category(models.Model):
    name = models.CharField(max_length=150, verbose_name='наименование категории')
    desc = models.TextField(verbose_name='описание категории')



    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов


class Contact(models.Model):
    name = models.CharField(max_length=150, verbose_name='имя')
    tel = models.CharField(max_length=50, verbose_name='телефон')
    message = models.CharField(max_length=500, verbose_name='сообщение')


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}, {self.tel}, {self.message}'

    class Meta:
        verbose_name = 'контакт' # Настройка для наименования одного объекта
        verbose_name_plural = 'контакты' # Настройка для наименования набора объектов


