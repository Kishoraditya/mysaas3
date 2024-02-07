# socialapp/views.py
from django.urls import reverse
import requests
from django.shortcuts import render, redirect
from django.views.generic import TemplateView
from django.conf import settings
from django.views import View
from allauth.socialaccount.models import SocialAccount
from django.contrib import messages

class ConnectToInstagramView(View):
    def get(self, request, *args, **kwargs):
        # Step 1: Redirect the user to Instagram for authorization
        authorization_url = f'https://api.instagram.com/oauth/authorize?client_id={settings.INSTAGRAM_APP_ID}&redirect_uri={settings.INSTAGRAM_REDIRECT_URI}&scope=user_profile,user_media&response_type=code'
        return redirect(authorization_url)

class InstagramCallbackView(View):
    def get(self, request, *args, **kwargs):
        # Step 2: Handle the callback after the user authorizes your app
        code = request.GET.get('code')
        if code:
            # Exchange the code for an access token
            token_url = 'https://api.instagram.com/oauth/access_token'
            data = {
                'client_id': settings.INSTAGRAM_APP_ID,
                'client_secret': settings.INSTAGRAM_APP_SECRET,
                'grant_type': 'authorization_code',
                'redirect_uri': settings.INSTAGRAM_REDIRECT_URI,
                'code': code,
            }
            response = requests.post(token_url, data=data)
            access_token = response.json().get('access_token')

            # Store or use the access_token as needed
            # For example, you can make API requests using the access_token
            # Store or use the access_token as needed
            # For example, you can make API requests using the access_token

            # Redirect to the ReportView and display Instagram information
            if access_token:
                # Store or use the access_token as needed
                # For example, you can make API requests using the access_token
                request.session['instagram_access_token'] = access_token
                messages.success(request, 'Successfully connected to Instagram!')
                return redirect(reverse('socialapp:report'))

        # Handle the case where the code is not present or invalid
        messages.error(request, 'Failed to connect to Instagram. Please try again.')
        return redirect(reverse('socialapp:connect_instagram'))
        #return redirect('socialapp:report')
    
class ConnectToSocialsView(TemplateView):
    template_name = 'socialapp/connect_socials.html'


class ReportView(TemplateView):
    template_name = 'socialapp/report.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        # Retrieve Instagram access token from session or query parameters
        access_token = self.request.session.get('instagram_access_token')

        if not access_token:
        # Redirect or handle the case where the access token is not present
            messages.error(self.request, 'Instagram access token not found.')
            return render(self.request, self.template_name, context)
        # Fetch Instagram account JSON data
        # Fetch Instagram account JSON data using the access token
        instagram_data = self.fetch_instagram_data(access_token)
        context['instagram_data'] = instagram_data

        return context

    def fetch_instagram_data(self, access_token):
        # Fetch Instagram account data using the access token
        url = 'https://graph.instagram.com/v11.0/me?fields=id,username&&access_token={access_token}'
        response = requests.get(url)
        data = response.json()
        return data


    