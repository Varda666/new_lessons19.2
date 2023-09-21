from django.shortcuts import render
from catalog.models import Product
from django.core.paginator import Paginator


# Create your views here.

def catalog_home(request):
    product_list = Product.objects.all
    context = {
        "object_list": product_list
    }
    return render(request, 'home.html', context)


def catalog_contacts(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        print(f'{name}, {phone}, {message}')
    return render(request, 'contacts.html')



def catalog_contacts_post(request):
    messages_list = []
    message_dict = {}
    if request.method == 'POST':
        message_dict['name'] = request.POST.get('name')
        message_dict['phone'] = request.POST.get('phone')
        message_dict['message'] = request.POST.get('message')
        messages_list.append(message_dict)
    print(messages_list)
    return render(request, 'index.html')

def catalog_product(request):
    product_list = Product.objects.all
    paginator = Paginator(product_list, 1)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    return render(request, 'product.html', {'page_obj': page_obj})

def add_product(request):
    product_list = []
    product_dict = {}
    if request.method == 'POST':
        product_dict['name'] = request.POST.get('name')
        product_dict['desc'] = request.POST.get('desc')
        product_dict['cat'] = request.POST.get('cat')
        product_dict['price'] = request.POST.get('price')
        product_list.append(product_dict)
    Product.objects.bulk_create(product_list)
    return render(request, 'product_add.html')