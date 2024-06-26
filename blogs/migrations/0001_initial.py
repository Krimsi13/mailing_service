# Generated by Django 5.0.4 on 2024-05-28 19:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=150, verbose_name='Заголовок')),
                ('content', models.TextField(verbose_name='Содержимое')),
                ('image', models.ImageField(blank=True, null=True, upload_to='blogs/', verbose_name='Изображение')),
                ('views_count', models.IntegerField(default=0, verbose_name='Количество просмотров')),
                ('created_at', models.DateField(blank=True, null=True, verbose_name='Дата создания')),
                ('is_published', models.BooleanField(default=True, verbose_name='Опубликовано')),
            ],
            options={
                'verbose_name': 'Пост',
                'verbose_name_plural': 'Посты',
            },
        ),
    ]
