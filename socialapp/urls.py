# socialapp/urls.py
from django.urls import path
from .views import ReportView, ConnectToInstagramView, ConnectToSocialsView, InstagramCallbackView

app_name = 'socialapp'

urlpatterns = [
    path('report/', ReportView.as_view(), name='report'),
    path('connect-instagram/', ConnectToInstagramView.as_view(), name='connect_instagram'),
    path('instagram-callback/', InstagramCallbackView.as_view(), name='instagram_callback'),
    path('connect-socials/', ConnectToSocialsView.as_view(), name='connect_socials'),
]
