from django.db import models

from users.models import User

NULLABLE = {'blank': True, 'null': True}


class ClientService(models.Model):
    email = models.EmailField(max_length=150, unique=True, verbose_name="Почта")
    name = models.CharField(max_length=100, verbose_name="Имя")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество", **NULLABLE)
    surname = models.CharField(max_length=150, verbose_name='Фамилия')
    comment = models.TextField(verbose_name="Комментарий", **NULLABLE)
    # is_active = models.BooleanField(default=True)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец клиента", **NULLABLE)

    def __str__(self):
        return f"{self.name}, {self.email}"

    class Meta:
        verbose_name = "Клиент"
        verbose_name_plural = "Клиенты"
        ordering = ('surname',)


class Message(models.Model):
    title = models.CharField(max_length=100, verbose_name="Тема письма")
    body = models.TextField(verbose_name="Тело письма", **NULLABLE)

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец сообщения", **NULLABLE)

    def __str__(self):
        return f'{self.title} : {self.body}'

    class Meta:
        verbose_name = "Сообщение для рассылки"
        verbose_name_plural = "Сообщения для рассылки"


class MailingSettings(models.Model):

    FREQUENCY_CHOICES = [
        ('Раз в день', 'Once a Day'),
        ('Раз в неделю', 'Once a Week'),
        ('Раз в месяц', 'Once a Month'),
    ]

    STATUS_CHOICES = [
        ('Завершена', 'Completed'),
        ('Создана', 'Created'),
        ('Запущена', 'Started'),
    ]

    date_time = models.DateTimeField(verbose_name="Время рассылки", auto_now_add=True)
    periodicity = models.CharField(verbose_name="Периодичность", max_length=20, choices=FREQUENCY_CHOICES,
                                   default='Раз в день')
    status = models.CharField(verbose_name="Статус рассылки", max_length=20, choices=STATUS_CHOICES, default='Создана')

    clients = models.ManyToManyField(ClientService, verbose_name="Клиент")
    message = models.ForeignKey(Message, on_delete=models.CASCADE, verbose_name='Сообщение')

    owner = models.ForeignKey(User, on_delete=models.CASCADE, verbose_name="Владелец рассылки", **NULLABLE)

    def __str__(self):
        return f"{self.date_time},{self.periodicity}, {self.status}, {self.clients}"

    class Meta:
        verbose_name = "Настройка рассылки"
        verbose_name_plural = "Настройки рассылки"
        permissions = (
            ("set_settings_deactivate", "Can deactivate settings"),
        )
        ordering = ('date_time',)


class LogsAttempt(models.Model):
    last_attempt = models.DateField(verbose_name="Дата и время последней попытки", auto_now_add=True)
    status = models.CharField(max_length=200, verbose_name="Статус попытки", default='Отправлено')
    response_mail = models.CharField(max_length=200, verbose_name="Ответ почтового сервера", **NULLABLE)

    mailing_settings = models.ForeignKey(MailingSettings, on_delete=models.SET_NULL, **NULLABLE)

    def __str__(self):
        return f"{self.mailing_settings}, {self.last_attempt}, {self.status}"

    class Meta:
        verbose_name = "Попытка рассылки"
        verbose_name_plural = "Попытки рассылки"
