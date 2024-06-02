from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from mailings.forms import StyleFormMixin
from users.models import User


class UserRegisterForm(StyleFormMixin, UserCreationForm):
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


# class UserForm(StyleFormMixin, UserChangeForm):
#     """Класс формы пользователя"""
#
#     class Meta:
#         model = User
#         fields = (
#             "email",
#             # "first_name",
#             # "last_name",
#             "phone",
#             "is_active",
#         )


class UserUpdateForm(StyleFormMixin, UserChangeForm):
    class Meta:
        model = User
        fields = ("is_active",)
