from django import forms
from django.forms import BooleanField

from mailings.models import ClientService, MessageLetter, MailingSettings


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class ClientServiceForm(StyleFormMixin, forms.ModelForm):
    """Класс формы клиента"""

    class Meta:
        model = ClientService
        fields = "__all__"


class MessageLetterForm(StyleFormMixin, forms.ModelForm):
    """Класс формы сообщения"""

    class Meta:
        model = MessageLetter
        fields = "__all__"
        widgets = {
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):
    """Класс формы рассылки"""

    class Meta:
        model = MailingSettings
        fields = "__all__"
