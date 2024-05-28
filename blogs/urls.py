from django.urls import path

from blogs.apps import BlogsConfig

app_name = BlogsConfig.name

urlpatterns = [
    # path("", BlogListView.as_view(), name="blog_list"),
]
