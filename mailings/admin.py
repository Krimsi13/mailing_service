from django.contrib import admin

from mailings.models import ClientService, Message, MailingSettings, LogsAttempt


@admin.register(ClientService)
class ClientServiceAdmin(admin.ModelAdmin):
    list_display = ('name', 'surname', 'email',)


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ('title', 'body',)


@admin.register(MailingSettings)
class MailingSettingsAdmin(admin.ModelAdmin):
    list_display = ('date_time', 'periodicity', 'status',)


@admin.register(LogsAttempt)
class LogsAttemptAdmin(admin.ModelAdmin):
    list_display = ('mailing_settings', 'last_attempt', 'status',)
