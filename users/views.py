import secrets

from django.contrib.auth.mixins import PermissionRequiredMixin, LoginRequiredMixin
from django.core.mail import send_mail
from django.shortcuts import get_object_or_404, redirect
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView, ListView, UpdateView

from config.settings import EMAIL_HOST_USER
from users.forms import UserRegisterForm, UserUpdateForm
from users.models import User


class UserCreateView(CreateView):
    model = User
    form_class = UserRegisterForm
    success_url = reverse_lazy('users:login')

    def form_valid(self, form):
        user = form.save()
        user.is_active = False
        token = secrets.token_hex(16)
        user.token = token
        user.save()
        host = self.request.get_host()
        url = f'http://{host}/users/email-confirm/{token}/'
        send_mail(
            subject="Подтверждение почты",
            message=f"Подтвердите вашу почту по ссылке: {url}",
            from_email=EMAIL_HOST_USER,
            recipient_list=[user.email],
        )
        return super().form_valid(form)


def email_verification(request, token):
    user = get_object_or_404(User, token=token)
    user.is_active = True
    user.save()
    return redirect(reverse("users:login"))


class UserListView(PermissionRequiredMixin, ListView):
    """Список всех пользователей, кроме самого себя и админа"""

    permission_required = ('users.view_all_user',)
    # permission_required = "view_all_user"
    model = User

    def get_queryset(self):
        return (
            super()
            .get_queryset()
            .exclude(pk=self.request.user.pk)
            .exclude(is_superuser=True)
        )


# class UserUpdateView(LoginRequiredMixin, UpdateView):
#     """обновление данных пользователя"""
#
#     model = User
#     form_class = UserUpdateForm  # форма для обновления данных
#     success_url = reverse_lazy("mailings:main_page")

    # def get_object(self, queryset=None):
    #     return self.request.user


class UserUpdateView(UpdateView):
    model = User
    template_name = "users/update_user.html"
    form_class = UserUpdateForm
    success_url = reverse_lazy("users:users_list")

    def get_object(self, queryset=None):
        return self.request.user

    def get_form_class(self):
        user = self.request.user
        if self.request.user.is_staff and user.has_perm("users.set_user_deactivate"):
            return UserUpdateForm
        else:
            return self.form_class
