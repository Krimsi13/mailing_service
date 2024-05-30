from django.shortcuts import render
from django.contrib.auth.mixins import PermissionRequiredMixin
from django.urls import reverse, reverse_lazy
from django.views.generic import CreateView, ListView, DetailView, UpdateView, DeleteView

from blogs.forms import BlogForm
from blogs.models import Blog


class BlogCreateView(PermissionRequiredMixin, CreateView):
    """Класс создания статьи блога"""

    form_class = BlogForm
    template_name = "blogs/blog_form.html"
    permission_required = "blogs.add_blog"
    success_url = reverse_lazy("blogs:blog_list")


class BlogListView(ListView):
    model = Blog
    extra_context = {
        'title': 'Блоги'
    }

    def get_queryset(self, *args, **kwargs):
        queryset = super().get_queryset(*args, **kwargs)
        queryset = queryset.filter(is_published=True)
        return queryset


class BlogDetailView(DetailView):
    model = Blog

    def get_object(self, queryset=None):
        self.object = super().get_object(queryset)
        self.object.views_count += 1
        self.object.save()
        return self.object


class BlogUpdateView(PermissionRequiredMixin, UpdateView):
    """Класс редактирования статьи блога"""
    model = Blog

    form_class = BlogForm
    template_name = "blogs/blog_form.html"
    permission_required = "blogs.change_blog"

    def get_success_url(self):
        return reverse("blogs:blog_view", args=[self.kwargs.get("pk")])


class BlogDeleteView(PermissionRequiredMixin, DeleteView):
    """Класс удаления статьи блога"""

    permission_required = "blogs.delete_blog"
    model = Blog
    success_url = reverse_lazy("blogs:blog_list")
