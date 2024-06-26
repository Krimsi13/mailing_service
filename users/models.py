from django.contrib.auth.models import AbstractUser
from django.db import models

NULLABLE = {'null': True, 'blank': True}


class User(AbstractUser):
    username = None
    email = models.EmailField(unique=True, verbose_name="Email", max_length=255)

    avatar = models.ImageField(upload_to='users/avatars', verbose_name="Аватар", **NULLABLE, help_text="Загрузите "
                                                                                                       "свой аватар")
    phone = models.CharField(max_length=35, verbose_name="Телефон", **NULLABLE, help_text="Введите номер телефона")
    country = models.CharField(max_length=255, verbose_name="Страна", **NULLABLE, help_text="Введите свою страну")

    token = models.CharField(max_length=100, verbose_name="Токен", **NULLABLE)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    class Meta:
        verbose_name = 'Пользователь'
        verbose_name_plural = 'Пользователи'
        permissions = (
            ("set_user_deactivate", "Can deactivate user"),
            ("view_all_user", "Can view all user"),
        )

    def __str__(self):
        return self.email

