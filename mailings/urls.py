from django.urls import path

from mailings.apps import MailingsConfig
from mailings.views import MailingSettingsListView, MailingSettingsDetailView, MailingSettingsUpdateView, \
    MailingSettingsDeleteView, MailingSettingsCreateView, ClientServiceListView, ClientServiceDetailView, \
    ClientServiceCreateView, ClientServiceUpdateView, ClientServiceDeleteView

app_name = MailingsConfig.name

urlpatterns = [
    # path('', ListView.as_view(), name='_list'),

    path("settings/", MailingSettingsListView.as_view(), name="settings"),
    path("settings/<int:pk>/", MailingSettingsDetailView.as_view(), name="settings_detail"),
    path("settings/create/", MailingSettingsCreateView.as_view(), name="settings_create"),
    path("settings/<int:pk>/update/", MailingSettingsUpdateView.as_view(), name="settings_update"),
    path("settings/<int:pk>/delete/", MailingSettingsDeleteView.as_view(), name="settings_delete"),

    path("clients/", ClientServiceListView.as_view(), name="clients"),
    path("clients/<int:pk>/", ClientServiceDetailView.as_view(), name="clients_detail"),
    path("clients/create/", ClientServiceCreateView.as_view(), name="clients_create"),
    path("clients/<int:pk>/update/", ClientServiceUpdateView.as_view(), name="clients_update"),
    path("clients/<int:pk>/delete/", ClientServiceDeleteView.as_view(), name="clients_delete"),
]