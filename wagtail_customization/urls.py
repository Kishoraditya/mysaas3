# wagtail_customization/urls.py
from django.urls import  path
from wagtail.contrib.settings import views as wagtailsettings_views

urlpatterns = [
    # ... other patterns ...
    path('wagtailsettings/', wagtailsettings_views.index, name='wagtailsettings_index'),
    # ... other patterns ...
]
