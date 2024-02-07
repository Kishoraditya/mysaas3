# userauth/views.py
from django.shortcuts import render
from django.views.generic import TemplateView
from allauth.account.views import LoginView, LogoutView, PasswordResetView, SignupView
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin


class SignUpView(SignupView):
    template_name = 'userauth/signup.html'

class CustomLoginView(LoginView):
    template_name = 'userauth/login.html'

class CustomLogoutView(LogoutView):
    template_name = 'userauth/logout.html'

class CustomPasswordResetView(PasswordResetView):
    template_name = 'userauth/password_reset.html'

class ProfileView(LoginRequiredMixin, TemplateView):
    template_name = 'userauth/profile.html'

