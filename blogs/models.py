from django.db import models

NULLABLE = {"null": True, "blank": True}


class Blog(models.Model):
    title = models.CharField(max_length=150, verbose_name="Заголовок")
    content = models.TextField(verbose_name="Содержимое")
    image = models.ImageField(upload_to="blogs/", **NULLABLE, verbose_name="Изображение")
    views_count = models.IntegerField(default=0, verbose_name="Количество просмотров")
    created_at = models.DateField(**NULLABLE, verbose_name="Дата создания")
    is_published = models.BooleanField(default=True, verbose_name="Опубликовано")

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Пост"
        verbose_name_plural = "Посты"
