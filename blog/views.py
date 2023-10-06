from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView
from blog.models import BlogMaterial


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
