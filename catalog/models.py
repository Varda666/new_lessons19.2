from django.db import models

# Create your models here.
class Product(models.Model):
    prod_name = models.CharField(max_length=150, verbose_name='наименование')
    prod_desc = models.CharField(max_length=500, verbose_name='описание')
    prod_imd = models.ImageField(upload_to='media/', verbose_name='изображение')
    prod_cat = models.CharField(max_length=150, verbose_name='категория')
    prod_price = models.PositiveIntegerField(verbose_name='цена за покупку')
    prod_create = models.DateTimeField(verbose_name='дата создания')
    prod_change = models.DateTimeField(verbose_name='дата последнего изменения')

    def __str__(self):
        # Строковое отображение объекта
        return f'{self.prod_name}'

    class Meta:
        verbose_name = 'товар' # Настройка для наименования одного объекта
        verbose_name_plural = 'товары' # Настройка для наименования набора объектов


class Category(models.Model):
    cat_name = models.CharField(max_length=150, verbose_name='наименование категории')
    cat_desc = models.CharField(max_length=500, verbose_name='описание категории')



    def __str__(self):
        # Строковое отображение объекта
        return f'{self.cat_name}'

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов


class Contact(models.Model):
    contact_name = models.CharField(max_length=150, verbose_name='имя')
    contact_tel = models.CharField(max_length=50, verbose_name='телефон')
    contact_message = models.CharField(max_length=500, verbose_name='сообщение')


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.contact_name}, {self.contact_tel}, {self.contact_message}'

    class Meta:
        verbose_name = 'контакт' # Настройка для наименования одного объекта
        verbose_name_plural = 'контакты' # Настройка для наименования набора объектов