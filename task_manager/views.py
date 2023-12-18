from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.utils.translation import gettext_lazy as _


class LogIn(SuccessMessageMixin, LoginView):
    form_class = AuthenticationForm
    template_name = 'user/login.html'
    success_message = _('Successfully login')
    success_url = reverse_lazy('/')


class LogOut(SuccessMessageMixin, LogoutView):
    success_url = reverse_lazy('/')
    success_message = _("Logged out")

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('Logger out'))
        return super().dispatch(request, *args, **kwargs)
