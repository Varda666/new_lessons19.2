from django.conf import settings
from django.core.cache import cache
from django.forms import inlineformset_factory


from catalog.forms import ProductForm, VersionForm
from catalog.models import Product, Contact, Category, Version
from django.urls import reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin

from catalog.services import get_cached_categories


class ProductCreateView(LoginRequiredMixin, PermissionRequiredMixin, CreateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.add_product'
    success_url = reverse_lazy('catalog:list')

    # def get_queryset(self, *args, **kwargs):
    #     return Product.user.filter(is_verificated=True, is_activated=True)


class ProductListView(ListView):
    model = Product

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        context_data['category'] = get_cached_categories()
        return context_data


    # def get_queryset(self, *args, **kwargs):
    #     queryset = super().get_queryset(*args, **kwargs)
    #     queryset = queryset.filter(published=True)
    #     return queryset


class ProductDetailView(PermissionRequiredMixin, DetailView):
    model = Product
    form_class = ProductForm
    success_url = reverse_lazy('catalog:detail')
    permission_required = 'catalog.view_product'

    # def get_object(self, queryset=None):
    #     self.object = super().get_object(queryset)
    #     self.object.views_count += 1
    #     self.object.save()
    #     return self.object

    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        if settings.CACHE_ENABLED:
            version_list = cache.get(f'version_list_{self.object.pk}')
            if version_list is None:
                version_list = self.object.version_set.all()
                cache.set(f'{self.object.pk}', version_list)
        else:
            version_list = self.object.version_set.all()
        context_data['versions'] = version_list
        return context_data




class ProductUpdateView(LoginRequiredMixin, PermissionRequiredMixin, UpdateView):
    model = Product
    form_class = ProductForm
    permission_required = 'catalog.change_product'


    def get_context_data(self, **kwargs):
        context_data = super().get_context_data(**kwargs)
        FormSet = inlineformset_factory(Product, Version, form=VersionForm, extra=1)
        if self.request.method == 'POST':
            formset = FormSet(self.request.POST, instance=self.object)
        else:
            formset = FormSet(instance=self.object)
        context_data['formset'] = formset
        return context_data

    def form_valid(self, form):
        context_data = self.get_context_data()
        formset = context_data['formset']
        self.object = form.save()

        if formset.is_valid():
                formset.instance = self.object
                formset.save()
        return super().form_valid(form)


class ProductDeleteView(LoginRequiredMixin, DeleteView):
    model = Product
    permission_required = 'catalog.delete_product'



class ContactCreateView(CreateView):
    model = Contact
    fields = ('name', 'tel', 'message')





# def catalog_home(request):
#     product_list = Product.objects.all()
#     context = {
#         "object_list": product_list,
#
#     }
#     return render(request, 'product_list.html', context)
#
#
# def catalog_contacts(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         phone = request.POST.get('phone')
#         message = request.POST.get('message')
#         Contact.objects.create(name=name, tel=phone, message=message)
#     return render(request, 'contact_form.html')
#
#
# def catalog_product(request, pk):
#     # paginator = Paginator(product_list, 1)
#     # page_number = request.GET.get('page')
#     # page_obj = paginator.get_page(page_number)?  {'page_obj': page_obj}
#     context = {
#         "object_list": Product.objects.filter(pk=pk)
#     }
#     return render(request, 'product_detail.html', context)
#
#
# def add_product(request):
#     if request.method == 'POST':
#         name = request.POST.get('name')
#         desc = request.POST.get('desc')
#         price = request.POST.get('price')
#         cat = request.POST.get('cat')
#         cat1, _ = Category.objects.get_or_create(name='Овощи', defaults={
#             "desc": "Описание категории овощи"
#         })
#         cat2, _ = Category.objects.get_or_create(name='Фрукты', defaults={
#             "desc": "Описание категории фрукты"
#         })
#         imd = request.POST.get('imd')
#         if str(cat) == str(cat1):
#             Product.objects.create(name=name, desc=desc, cat=cat1, price=price, imd=imd)
#         elif str(cat) == str(cat2):
#             Product.objects.create(name=name, desc=desc, cat=cat2, price=price, imd=imd)
#
#     return render(request, 'product_form.html')