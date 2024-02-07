from django.conf import settings
from django.urls import include, path
from django.contrib import admin

from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail.documents import urls as wagtaildocs_urls
from wagtail.contrib.settings import urls as wagtailsettings_urls

from search import views as search_views
from userauth.views import SignUpView, CustomLoginView, CustomLogoutView, CustomPasswordResetView, ProfileView
from socialapp.views import ConnectToInstagramView, ReportView, ConnectToSocialsView

urlpatterns = [
    path("django-admin/", admin.site.urls),
    path('accounts/', include('allauth.urls')),
    path('userauth/', include('userauth.urls')),
    path('profile/', ProfileView.as_view(), name='account_profile'),
    path('signup/', SignUpView.as_view(), name='signup'),
    path('login/', CustomLoginView.as_view(), name='login'),
    path('logout/', CustomLogoutView.as_view(), name='logout'),
    path('password-reset/', CustomPasswordResetView.as_view(), name='password_reset'),
    path('socialapp/', include('socialapp.urls', namespace='socialapp')),
    #path('socialapp/report/', ReportView.as_view(), name='socialapp_report'),
    #path('socialapp/connect-instagram/', ConnectToInstagramView.as_view(), name='socialapp_connect_instagram'),
    #path('socialapp/connect-socials/', ConnectToSocialsView.as_view(), name='socialapp_connect_socials'),
    path("search/", search_views.search, name="search"),
    path("admin/", include(wagtailadmin_urls)),
    path("documents/", include(wagtaildocs_urls)),
    path('admin/snippets/wagtail_customization/', include(wagtailsettings_urls)),
    
    
]


if settings.DEBUG:
    from django.conf.urls.static import static
    from django.contrib.staticfiles.urls import staticfiles_urlpatterns

    # Serve static and media files from development server
    urlpatterns += staticfiles_urlpatterns()
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

urlpatterns = urlpatterns + [
    # For anything not caught by a more specific rule above, hand over to
    # Wagtail's page serving mechanism. This should be the last pattern in
    # the list:
    
    path("", include(wagtail_urls)),
    # Alternatively, if you want Wagtail pages to be served from a subpath
    # of your site, rather than the site root:
    #    path("pages/", include(wagtail_urls)),
]
