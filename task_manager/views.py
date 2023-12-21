from django.contrib import messages
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy
from django.utils.translation import gettext_lazy as _

from task_manager.forms import PlaceholderAuthForm


class LogIn(SuccessMessageMixin, LoginView):
    form_class = PlaceholderAuthForm
    template_name = 'form.html'
    success_message = _('Вы залогинены')
    success_url = reverse_lazy('index')
    extra_context = {
        'btn_text': _('Войти'),
        'title': _('Вход')
    }


class LogOut(SuccessMessageMixin, LogoutView):
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('Вы разлогинены'))
        return super().dispatch(request, *args, **kwargs)
