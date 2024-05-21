from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from mailings.models import MailingSettings, ClientService


class MailingSettingsListView(ListView):
    model = MailingSettings


class MailingSettingsDetailView(DetailView):
    model = MailingSettings


class MailingSettingsCreateView(CreateView):
    model = MailingSettings
    fields = '__all__'
    # form_class = MailingSettingsForm
    success_url = reverse_lazy("mailings:settings")


class MailingSettingsUpdateView(UpdateView):
    model = MailingSettings
    fields = '__all__'
    success_url = reverse_lazy("mailings:settings")


class MailingSettingsDeleteView(DeleteView):
    model = MailingSettings
    success_url = reverse_lazy("mailings:settings")


class ClientServiceListView(ListView):
    model = ClientService


class ClientServiceDetailView(DetailView):
    model = ClientService


class ClientServiceCreateView(CreateView):
    model = ClientService
    fields = '__all__'
    # form_class = ClientServiceForm
    success_url = reverse_lazy("mailings:clients")


class ClientServiceUpdateView(UpdateView):
    model = ClientService
    fields = '__all__'
    success_url = reverse_lazy("mailings:clients")


class ClientServiceDeleteView(DeleteView):
    model = ClientService
    success_url = reverse_lazy("mailings:clients")
