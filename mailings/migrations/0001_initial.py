# Generated by Django 5.0.4 on 2024-05-19 18:11

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ClientService',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=150, unique=True, verbose_name='Почта')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('patronymic', models.CharField(blank=True, max_length=100, null=True, verbose_name='Отчество')),
                ('surname', models.CharField(max_length=150, verbose_name='Фамилия')),
                ('comment', models.TextField(blank=True, null=True, verbose_name='Комментарий')),
            ],
            options={
                'verbose_name': 'Клиент',
                'verbose_name_plural': 'Клиенты',
                'ordering': ('surname',),
            },
        ),
        migrations.CreateModel(
            name='MessageLetter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, verbose_name='Тема письма')),
                ('body', models.TextField(blank=True, null=True, verbose_name='Тело письма')),
            ],
            options={
                'verbose_name': 'Сообщение для рассылки',
                'verbose_name_plural': 'Сообщения для рассылки',
            },
        ),
        migrations.CreateModel(
            name='MailingSettings',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_time', models.DateTimeField(auto_now_add=True, verbose_name='Время рассылки')),
                ('periodicity', models.CharField(choices=[('once_a_day', 'Once a Day'), ('once_a_week', 'Once a Week'), ('once_a_month', 'Once a Month')], default='once_a_day', max_length=20, verbose_name='Периодичность')),
                ('status', models.CharField(choices=[('completed', 'Completed'), ('created', 'Created'), ('started', 'Started')], default='created', max_length=20, verbose_name='Статус рассылки')),
                ('clients', models.ManyToManyField(to='mailings.clientservice', verbose_name='Клиент')),
                ('message', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mailings.messageletter', verbose_name='Сообщение')),
            ],
            options={
                'verbose_name': 'Настройка рассылки',
                'verbose_name_plural': 'Настройки рассылки',
                'ordering': ('date_time',),
            },
        ),
        migrations.CreateModel(
            name='LogsAttempt',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('last_attempt', models.DateField(auto_now_add=True, verbose_name='Дата и время последней попытки')),
                ('status', models.CharField(default='completed', max_length=200, verbose_name='Статус попытки')),
                ('response_mail', models.CharField(blank=True, max_length=200, null=True, verbose_name='Ответ почтового сервера')),
                ('mailing_settings', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='mailings.mailingsettings')),
            ],
            options={
                'verbose_name': 'Попытка рассылки',
                'verbose_name_plural': 'Попытки рассылки',
            },
        ),
    ]
