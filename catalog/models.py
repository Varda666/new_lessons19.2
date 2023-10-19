from django.db import models


class Category(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='наименование категории')
    desc = models.TextField(default='',verbose_name='описание категории')



    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = 'категория' # Настройка для наименования одного объекта
        verbose_name_plural = 'категории' # Настройка для наименования набора объектов


# Create your models here.
class Product(models.Model):
    name = models.CharField(max_length=150, unique=True, verbose_name='наименование')
    desc = models.TextField(default='', verbose_name='описание')
    imd = models.ImageField(upload_to='media/', default='media/Тыква.jpg', verbose_name='изображение')
    cat = models.ForeignKey('Category', to_field='name', on_delete=models.DO_NOTHING, verbose_name='категория')
    price = models.PositiveIntegerField(verbose_name='цена за покупку')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')
    updated_at = models.DateTimeField(auto_now=True, verbose_name='дата последнего изменения')
    user = models.ForeignKey('users.User', to_field='email', default='',  on_delete=models.DO_NOTHING, verbose_name='владелец')


    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = 'товар' # Настройка для наименования одного объекта
        verbose_name_plural = 'товары' # Настройка для наименования набора объектов


class Contact(models.Model):
    name = models.CharField(max_length=150, db_index=True, verbose_name='имя')
    tel = models.CharField(max_length=50, verbose_name='телефон')
    message = models.CharField(max_length=500, verbose_name='сообщение')


    def __str__(self):
        # Строковое отображение объекта
        return f'{self.name}, {self.tel}, {self.message}'

    class Meta:
        verbose_name = 'контакт' # Настройка для наименования одного объекта
        verbose_name_plural = 'контакты' # Настройка для наименования набора объектов


class Version(models.Model):
    num = models.PositiveIntegerField(unique=False, verbose_name='номер версии')
    name = models.CharField(max_length=150, verbose_name='название версии')
    prod = models.ForeignKey('Product', to_field='name', on_delete=models.DO_NOTHING, verbose_name='продукт')
    is_active = models.BooleanField(default=False, verbose_name='признак текущей версии')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='дата создания')

    def __str__(self):
        # Строковое отображение объекта
        return self.name

    class Meta:
        verbose_name = 'версия' # Настройка для наименования одного объекта
        verbose_name_plural = 'версии' # Настройка для наименования набора объектов