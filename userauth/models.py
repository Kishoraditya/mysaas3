# userauth/models.py
from django.db import models
from django.contrib.auth.models import AbstractUser
from socialapp.models import SocialAccount

class CustomUser(AbstractUser):
    social_account = models.OneToOneField(SocialAccount, on_delete=models.CASCADE, null=True, blank=True)
    # Add more fields as needed
