# Generated by Django 5.0.4 on 2024-06-02 13:32

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'permissions': (('set_user_deactivate', 'Can deactivate user'), ('view_all_user', 'Can view all user')), 'verbose_name': 'Пользователь', 'verbose_name_plural': 'Пользователи'},
        ),
    ]
