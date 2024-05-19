from django.urls import path

from mailings.apps import MailingsConfig
# from mailings.views import ListView

app_name = MailingsConfig.name

urlpatterns = [
    # path('', ListView.as_view(), name='_list'),
]
