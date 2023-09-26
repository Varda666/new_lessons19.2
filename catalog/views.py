from django.shortcuts import render
from catalog.models import Product, Contact, Category
from django.core.paginator import Paginator


# Create your views here.

def catalog_home(request):
    product_list = Product.objects.all()
    context = {
        "object_list": product_list,

    }
    return render(request, 'home.html', context)


def catalog_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        Contact.objects.create(name=name, tel=phone, message=message)
    return render(request, 'contacts.html')


def catalog_product(request, pk):
    # paginator = Paginator(product_list, 1)
    # page_number = request.GET.get('page')
    # page_obj = paginator.get_page(page_number)?  {'page_obj': page_obj}
    context = {
        "object_list": Product.objects.filter(pk=pk)
    }
    return render(request, 'product.html', context)


def add_product(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        desc = request.POST.get('desc')
        price = request.POST.get('price')
        cat = request.POST.get('cat')
        cat1, _ = Category.objects.get_or_create(name='Овощи', defaults={
            "desc": "Описание категории овощи"
        })
        cat2, _ = Category.objects.get_or_create(name='Фрукты', defaults={
            "desc": "Описание категории фрукты"
        })
        imd = request.POST.get('imd')
        if str(cat) == str(cat1):
            Product.objects.create(name=name, desc=desc, cat=cat1, price=price, imd=imd)
        elif str(cat) == str(cat2):
            Product.objects.create(name=name, desc=desc, cat=cat2, price=price, imd=imd)

    return render(request, 'product_add.html')