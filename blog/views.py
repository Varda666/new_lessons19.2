from django.core.mail import send_mail
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import BlogMaterial
from config import settings


class BlogMaterialCreateView(CreateView):
    model = BlogMaterial
    fields = ('name', 'slug', 'imd')
    success_url = reverse_lazy('blog:list')


class BlogMaterialListView(ListView):
    model = BlogMaterial


    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(published=True)
        return queryset


class BlogMaterialDetailView(DetailView):
    model = BlogMaterial
    fields = ('name', 'slug')
    success_url = reverse_lazy('blog:detail')

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object

    def send_mess_email(self, queryset):
        self.object = super().get_object(queryset)
        if self.object.views_count > 10:
            send_mail(
                subject='Поздравление',
                message='Поздравляем, у вас 10 просмотров',
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['Varda666@inbox.ru']
            )


class BlogMaterialUpdateView(UpdateView):
    model = BlogMaterial
    fields = ('name', 'slug')
    # success_url = reverse_lazy('blog:list')

    def get_success_url(self):
        return reverse('blog:view', args=[self.kwargs.get('pk')])

class BlogMaterialDeleteView(DeleteView):
    model = BlogMaterial
    success_url = reverse_lazy('blog:list')


# Create your views here.
