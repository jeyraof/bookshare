# -*- coding: utf-8 -*-

from django.conf import settings
from django.conf.urls import include, url
from django.conf.urls.static import static
from django.contrib import admin
from bookshare import views as bookshare_views

main_patterns = [
    url(r'^$', bookshare_views.main, name='main'),
    url(r'^settings', 'user_profile.views.settings'),
    url(r'^mail$', 'user_profile.views.mail'),
]

urlpatterns = [
    url(r'', include(main_patterns)),
    url(r'^user/', include('user_profile', namespace='user')),
    url(r'^book/', include('book.urls', namespace='book')),

    # API
    url(r'^api/v1/', include('api.urls', namespace='api_v1')),

    # Auth, default
    url(r'^logout/',
        'django.contrib.auth.views.logout',
        {'next_page': settings.LOGOUT_REDIRECT_URL},
        name='logout'),
    url('', include('social.apps.django_app.urls', namespace='social')),
    url(r'^admin/', include(admin.site.urls)),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.NODE_MODULES_URL, document_root=settings.NODE_MODULES_ROOT)
