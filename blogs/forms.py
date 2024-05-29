from django import forms

from blogs.models import Blog


class BlogForm(forms.ModelForm):
    """Класс формы для блога"""

    class Meta:
        model = Blog
        fields = ("title", "content", "image", "is_published")
