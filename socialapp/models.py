# socialapp/models.py
from django.db import models
from django.conf import settings

class SocialAccount(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='social_app_account')
    instagram_access_token = models.CharField(max_length=255, blank=True, null=True)
    facebook_access_token = models.CharField(max_length=255, blank=True, null=True)
    # Add more fields as needed
