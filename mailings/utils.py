import smtplib
from datetime import datetime, timedelta

import pytz
from django.core.mail import send_mail
from django.db.models import F

from config import settings
from mailings.models import MailingSettings, LogsAttempt


def test_print_time():
    time_zone = pytz.timezone(settings.TIME_ZONE)
    now = datetime.now(time_zone)
    print(f"Current time: {now}")


def send_mailing():
    periodicity = ["Раз в день", "Раз в неделю", "Раз в месяц"]
    zone = pytz.timezone(settings.TIME_ZONE)
    current_datetime = datetime.now(zone)
    mailings = MailingSettings.objects.filter(status="Запущена")

    for mailing in mailings:
        if mailing.date_time < current_datetime + timedelta(hours=3):
            status_interface = "Ошибка"
            server_response = "Нет ответа"

            try:
                send_mail(
                        subject=mailing.message.title,
                        message=mailing.message.body,
                        from_email=settings.EMAIL_HOST_USER,
                        recipient_list=[client.email for client in mailing.clients.all()],
                        fail_silently=False
                )
                if mailing.periodicity == periodicity[0]:
                    mailing.date_time = F('date_time') + timedelta(days=1)

                elif mailing.periodicity == periodicity[1]:
                    mailing.date_time = F('date_time') + timedelta(days=7)

                elif mailing.periodicity == periodicity[2]:
                    mailing.date_time = F('date_time') + timedelta(days=30)

                mailing.save()

                status_interface = "Отправлено"
                server_response = "Успешно"

            except smtplib.SMTPResponseException as e:
                status_interface = "Ошибка"
                server_response = str(e)

            finally:
                LogsAttempt.objects.create(
                    mailing_settings=mailing,
                    status=status_interface,
                    response_mail=server_response,
                )
