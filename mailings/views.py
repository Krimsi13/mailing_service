from random import sample

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import PermissionDenied
from django.shortcuts import render
from django.urls import reverse_lazy
from django.views.generic import ListView, DetailView, UpdateView, DeleteView, CreateView

from blogs.models import Blog
from mailings.forms import MailingSettingsForm, ClientServiceForm, MessageLetterForm, MailingSettingsManagerForm
from mailings.models import MailingSettings, ClientService, MessageLetter, LogsAttempt


def main_page(request):

    total_messages_count = MessageLetter.objects.count()
    active_logs_count = LogsAttempt.objects.count()
    active_clients_count = ClientService.objects.count()

    all_blogs = Blog.objects.all()
    random_blogs = sample(list(all_blogs), min(3, all_blogs.count()))

    context = {
        'total_messages_count': total_messages_count,
        'active_logs_count': active_logs_count,
        'active_clients_count': active_clients_count,
        'random_blogs': random_blogs,
        'title': 'Главная'
    }

    return render(request, 'mailings/main_page.html', context)


class MailingSettingsListView(ListView):
    extra_context = {
        'title': 'Рассылки'
    }
    model = MailingSettings


class MailingSettingsDetailView(LoginRequiredMixin, DetailView):
    model = MailingSettings


class MailingSettingsCreateView(LoginRequiredMixin, CreateView):
    model = MailingSettings
    # fields = '__all__'
    form_class = MailingSettingsForm
    success_url = reverse_lazy("mailings:settings")

    def form_valid(self, form):
        mailing_settings = form.save()
        user = self.request.user
        mailing_settings.owner = user
        mailing_settings.save()
        return super().form_valid(form)

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        kwargs.update({'request': self.request})
        return kwargs


class MailingSettingsUpdateView(LoginRequiredMixin, UpdateView):
    model = MailingSettings
    form_class = MailingSettingsForm
    # fields = '__all__'
    success_url = reverse_lazy("mailings:settings")

    def get_form_class(self):
        user = self.request.user
        if user == self.object.owner:
            return MailingSettingsForm
        if user.has_perm('mailings.set_settings_deactivate'):
            return MailingSettingsManagerForm
        raise PermissionDenied


class MailingSettingsDeleteView(LoginRequiredMixin, DeleteView):
    model = MailingSettings
    success_url = reverse_lazy("mailings:settings")


class ClientServiceListView(ListView):
    extra_context = {
        'title': 'Клиенты'
    }
    model = ClientService

    # на вкладке клиенты отображаются клиенты только пользователя(пока выключил)
    # def get_queryset(self):
    #     if self.request.user.is_superuser:
    #         return ClientService.objects.all()
    #     else:
    #         return ClientService.objects.filter(owner=self.request.user)


class ClientServiceDetailView(LoginRequiredMixin, DetailView):
    model = ClientService


class ClientServiceCreateView(CreateView):
    model = ClientService
    # fields = '__all__'
    form_class = ClientServiceForm
    success_url = reverse_lazy("mailings:clients")

    def form_valid(self, form):
        client_service = form.save()
        user = self.request.user
        client_service.owner = user
        client_service.save()
        return super().form_valid(form)


class ClientServiceUpdateView(LoginRequiredMixin, UpdateView):
    model = ClientService
    form_class = ClientServiceForm
    # fields = '__all__'
    success_url = reverse_lazy("mailings:clients")


class ClientServiceDeleteView(LoginRequiredMixin, DeleteView):
    model = ClientService
    success_url = reverse_lazy("mailings:clients")


class MessageLetterListView(ListView):
    extra_context = {
        'title': 'Сообщения'
    }
    model = MessageLetter


class MessageLetterDetailView(LoginRequiredMixin, DetailView):
    model = MessageLetter


class MessageLetterCreateView(LoginRequiredMixin, CreateView):
    model = MessageLetter
    # fields = '__all__'
    form_class = MessageLetterForm
    success_url = reverse_lazy("mailings:messages")

    def form_valid(self, form):
        message_letter = form.save()
        user = self.request.user
        message_letter.owner = user
        message_letter.save()
        return super().form_valid(form)


class MessageLetterUpdateView(LoginRequiredMixin, UpdateView):
    model = MessageLetter
    form_class = MessageLetterForm
    # fields = '__all__'
    success_url = reverse_lazy("mailings:messages")


class MessageLetterDeleteView(LoginRequiredMixin, DeleteView):
    model = MessageLetter
    success_url = reverse_lazy("mailings:messages")


class LogsAttemptListView(ListView):
    extra_context = {
        'title': 'Журнал рассылок'
    }
    model = LogsAttempt
