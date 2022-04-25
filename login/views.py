from django.http import HttpResponseRedirect
from django.urls import reverse  
from django.contrib.auth import login as auth_login
from django.contrib.auth.views import LoginView
from django.contrib import messages

from .registration_tools.signup import HomeAndSignupView
from .registration_tools.activate import Activate
from .registration_tools.change_password import ChangePassword


class HomeView(HomeAndSignupView):
    template_name = 'home.html'


class ActivateUserView(Activate):
    template_name = 'registration/confirmed_account.html'


class ChangePasswordView(ChangePassword):
    template_name = 'registration/change_password.html'


class Login(LoginView):
    def form_valid(self, form):
        auth_login(self.request, form.get_user())
        if form.get_user().is_first_connection:
            messages.info(self.request, 'This is your first connection with this account, please change your password')
            return HttpResponseRedirect(reverse('change_password'))
        else:
            return HttpResponseRedirect(self.get_success_url())
