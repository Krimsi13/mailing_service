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
        # fields = "__all__"
        exclude = ["owner"]


class MessageLetterForm(StyleFormMixin, forms.ModelForm):
    """Класс формы сообщения"""

    class Meta:
        model = MessageLetter
        # fields = "__all__"
        exclude = ["owner"]
        widgets = {
            "subject": forms.TextInput(attrs={"class": "form-control"}),
            "body": forms.Textarea(attrs={"class": "form-control"}),
        }


class MailingSettingsForm(StyleFormMixin, forms.ModelForm):
    """Класс формы рассылки"""
    # вариант 1(не сработал)
    # def __init__(self, *args, **kwargs):
    #     self.owner = kwargs.pop('owner', None)
    #     self.request = kwargs.pop('request', None)
    #     super(MailingSettingsForm, self).__init__(*args, **kwargs)
    #     self.fields['clients'].queryset = ClientService.objects.filter(owner=self.request.user)

    # вариант 2(не сработал)
    # def __init__(self, *args, **kwargs):
    #     self.request = kwargs.pop('request')
    #     user = self.request.user
    #     super().__init__(self, *args, **kwargs)
    #     self.fields['clients'].queryset = ClientService.objects.filter(owner=self.request.user)

    # вариант 3(сработал)
    def __init__(self, *args, **kwargs):
        # Получаем текущего пользователя из kwargs
        self.request = kwargs.pop('request', None)
        super().__init__(*args, **kwargs)

        # Фильтруем поле clients только для тех клиентов, которые принадлежат текущему пользователю
        if self.request and self.request.user:
            self.fields['clients'].queryset = ClientService.objects.filter(owner=self.request.user)
            self.fields['message'].queryset = MessageLetter.objects.filter(owner=self.request.user)

    class Meta:
        model = MailingSettings
        fields = "__all__"
        exclude = ["owner"]
