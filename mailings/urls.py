from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import MailingSettingsListView, MailingSettingsDetailView, MailingSettingsUpdateView, \
    MailingSettingsDeleteView, MailingSettingsCreateView

app_name = MailingsConfig.name

urlpatterns = [
    # path('', ListView.as_view(), name='_list'),
    path("settings/", MailingSettingsListView.as_view(), name="settings"),
    path("settings/<int:pk>/", MailingSettingsDetailView.as_view(), name="settings_detail"),
    path("settings/create/", MailingSettingsCreateView.as_view(), name="settings_create"),
    path("settings/<int:pk>/update/", MailingSettingsUpdateView.as_view(), name="settings_update"),
    path("settings/<int:pk>/delete/", MailingSettingsDeleteView.as_view(), name="settings_delete"),
]
