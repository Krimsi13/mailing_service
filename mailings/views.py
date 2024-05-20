from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from mailings.models import MailingSettings


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
