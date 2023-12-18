from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.messages.views import SuccessMessageMixin
from django.urls import reverse_lazy

from django.utils.translation import gettext_lazy as _

from task_manager.forms import PlaceholderAuthForm


class LogIn(SuccessMessageMixin, LoginView):
    form_class = PlaceholderAuthForm
    template_name = 'form.html'
    success_message = _('Successfully login')
    success_url = reverse_lazy('index')
    extra_context = {
        'btn_text': _('login'),
        'title': _('log in')
    }


class LogOut(SuccessMessageMixin, LogoutView):
    success_url = reverse_lazy('index')

    def dispatch(self, request, *args, **kwargs):
        messages.info(request, _('Logger out'))
        return super().dispatch(request, *args, **kwargs)
